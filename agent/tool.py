import streamlit as st
import pandas as pd
import clickhouse_driver
from io import StringIO
import sys
from langchain_experimental.utilities import PythonREPL

class StatefulPythonREPL(PythonREPL):
    def __init__(self):
        super().__init__()
        self.globals = {}
    
    def run(self, command: str) -> str:
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        try:
            exec(command, self.globals)
            sys.stdout = old_stdout
            output = mystdout.getvalue()
        except Exception as e:
            sys.stdout = old_stdout
            output = f"Error: {str(e)}"
        return output.strip()

def generate_df_summary(df: pd.DataFrame) -> str:
    if df.empty:
        return "查询结果为空"
    
    summary = [
        f"📊 数据摘要（共 {len(df)} 行）",
        f"📑 列名称：{', '.join(df.columns)}"
    ]
    
    # 添加列类型信息
    type_info = [f"{col}: {dtype}" for col, dtype in df.dtypes.items()]
    summary.append(f"🔧 列类型：{' | '.join(type_info)}")
    
    # 添加数值列统计信息
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        summary.append(
            f"📈 {col}统计：均值={df[col].mean():.2f} "
            f"最小={df[col].min():.2f} "
            f"最大={df[col].max():.2f}"
        )
    
    # 添加示例数据
    summary.append("🔍 前2行示例：")
    summary.append(df.head(2).to_string(index=False))
    
    return "\n\n".join(summary)

# ClickHouse SQL执行函数
def execute_sql(query: str) -> pd.DataFrame:
    db_con = clickhouse_driver.Client(
        host='ap.loclx.io',
        port=46749,
        user='communal',
        password=st.session_state.clickhouse_password,
        database='crsp',
        settings={'use_numpy': True}
    )
    df, types=db_con.execute(query,with_column_types=True)
    df2=pd.DataFrame(df) # convert df to dataframe
    df2.columns=[x[0] for x in types] # retrieve columns to the dataframe
    return df2