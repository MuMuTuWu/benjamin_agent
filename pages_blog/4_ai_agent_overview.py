import streamlit as st

st.title("🌐 From LLMs to Agents")

st.markdown("""### **1. Workflow-driven Agents**

Provides visual tools and modular frameworks to build reusable AI workflows for enterprises. Achieve task automation through visual process design, emphasizing rule orientation and modular expansion.

- **AI Development Platform**: Dify (an open-source LLM application building platform), Coze (a dedicated platform for chatbots)
	- Intuitive low-code workflow orchestration for non-coders, Visual RAG engine, and supports multi-model scheduling.
- **Image Workflow Tools**: ComfyUI (Open-source platform for AI-generated images and videos via visual node-based workflows.)
    - Core capabilities: Highly customizable for Stable Diffusion models, Supports complex generative pipelines.

##### Workflow: Prompt chaining

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.png&w=3840&q=75)

##### Workflow: Routing

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5c0c0e9fe4def0b584c04d37849941da55e5e71c-2401x1000.png&w=3840&q=75)

##### Workflow: Parallelization

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F406bb032ca007fd1624f261af717d70e6ca86286-2401x1000.png&w=3840&q=75)

##### Workflow: Orchestrator-workers

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8985fc683fae4780fb34eab1365ab78c7e51bc8e-2401x1000.png&w=3840&q=75)

##### Workflow: Evaluator-optimizer

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F14f51e6406ccb29e695da48b17017e899a6119c7-2401x1000.png&w=3840&q=75)

### 2. AI for Software Engineering

These tools focus on programming assistance and are suitable for developers to improve productivity.

- **Cursor** (an enhanced version of VS Code), **GitHub** Copilot (real-time code suggestions)
	- **Agent Mode:** Autonomous code generation and refactoring.
	- **Completion and Chat Mode:** Contextual understanding of codebases. Assists with code generation, completion, and debugging, understanding developer intent.

##### High-level flow of a coding agent

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F4b9a1f4eb63d5962a6e1746ac26bbc857cf3474f-2400x1666.png&w=3840&q=75)

### **3. In-depth Research Agents**

Focused on deep information retrieval and multi-step reasoning, integrating online search and analysis to generate professional research reports with citations.

- **Perplexity/ChatGPT/Gemini/Grok**: They have in-depth research functions based on RAG, supporting multi-source verification and structured output.
	1. Broad Knowledge Base: Excels in diverse topics due to extensive training data, improving contextual analysis.
	2. Polished Outputs: Generates more natural, human-like reports with refined language.
	3. Robust Reasoning: Handles complex queries with nuanced understanding, especially for ambiguous topics.

### **4. General-purpose Autonomous Agents**

These agents possess the capabilities of **autonomous decision-making** and **cross-domain task execution**.

- **Manus AI**: It supports multi-modal processing of text, images, and code, and can independently complete complex tasks such as report writing and itinerary planning.
- **AutoGLM**: An open-source general-purpose agent framework that supports tool invocation and continuous learning (assuming a similar architecture to Manus).

##### Autonomous agent

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F58d9f10c985c4eb5d53798dea315f7bb5ab6249e-2401x1000.png&w=3840&q=75)""")

st.markdown("### 💰 It's very costly to get the cutting-edge AI-Agents")

col1, col2 = st.columns([0.3, 0.7], gap="small")
with col1:
    st.image("assets/cost gpt pro.png", caption="ChatGPT Pro")
with col2:
    st.image("assets/cost manus.png", caption="Manus AI")

st.subheader("📖 Summary")

st.markdown("""|                             | Workflow-driven AI-Agent                                                    | General AI-Agent                                            |
| --------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Core Capability**         | Model-driven structured workflows, multi-model collaboration               | Dynamic task orchestration, external resource interaction   |
| **Usage Scenarios**         | Structured business workflows (e.g., customer service, command management) | Personalized long-term scenarios (e.g., planning, research) |
| **User Base**               | Requires significant team effort                                           | Individual users can quickly adopt                          |
| **Execution Style**         | Human-driven, iterative optimization                                       | Autonomous, multi-step reasoning                            |
| **Strengths**               | High scalability, rapid development                                        | Flexibility, autonomous operation                           |
| **Weaknesses**              | Limited flexibility, resource-intensive                                    | Scalability limitations, resource dependency                |
""")