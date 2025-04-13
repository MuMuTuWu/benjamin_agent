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
        return "Query result is empty"
    
    summary = [
        f"📊 Data Summary (Total {len(df)} rows)",
        f"📑 Column Names: {', '.join(df.columns)}"
    ]
    
    # Add column type information
    type_info = [f"{col}: {dtype}" for col, dtype in df.dtypes.items()]
    summary.append(f"🔧 Column Types: {' | '.join(type_info)}")
    
    # Add numeric column statistics
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        summary.append(
            f"📈 {col} Statistics: Mean={df[col].mean():.2f} "
            f"Min={df[col].min():.2f} "
            f"Max={df[col].max():.2f}"
        )
    
    # Add sample data - dynamically adjust display rows based on column and row count
    num_cols = len(df.columns)
    num_rows = len(df)
    
    if num_cols < 5:
        head_rows = tail_rows = min(5, num_rows // 2)
    elif num_cols < 10:
        head_rows = tail_rows = min(3, num_rows // 2)
    else:
        head_rows = tail_rows = min(2, num_rows // 2)
    
    if num_rows <= (head_rows + tail_rows):
        summary.append(f"🔍 All {num_rows} rows of data:")
        summary.append(df.to_string(index=False))
    else:
        summary.append(f"🔍 First {head_rows} rows sample:")
        summary.append(df.head(head_rows).to_string(index=False))
        
        if tail_rows > 0:
            summary.append(f"🔍 Last {tail_rows} rows sample:")
            summary.append(df.tail(tail_rows).to_string(index=False))
    
    return "\n\n".join(summary)

# ClickHouse SQL execution function
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