🤖 AI App Builder (Lovable Clone)
An AI-powered application builder that generates full project structures from natural language instructions.
This project replicates the core idea of Lovable — users simply describe what they want to build, and the system automatically plans, structures, and generates project files using AI agents.
🚀 Features
🧠 Multi-Agent Architecture (Planner → Architect → Coder)
📝 Natural Language → Full Project Generation
📂 Automatic File Creation & Project Structuring
🔁 Step-by-step Implementation Execution
📱 Responsive Mobile-Friendly UI (Streamlit)
⚡ Groq LLM Integration for fast inference
🛠 Tool-based File System Execution
🏗 Architecture Overview
This project uses a LangGraph multi-agent workflow:
Planner Agent
Converts user prompt into structured Plan
Defines app name, tech stack, features, and file structure
Architect Agent
Breaks the plan into implementation steps
Creates structured TaskPlan
Coder Agent
Iterates through each step
Reads existing files
Generates full updated file content
Writes files using safe project tools
🛠 Tech Stack
Python
Streamlit (Frontend UI)
LangGraph
LangChain
Groq API (LLaMA models)
Pydantic (Structured Outputs)
dotenv
Custom Tool System (read/write/run commands)
📂 Project Structure
Copy code

appbuilder/
│
├── agent/
│   ├── graph.py
│   ├── prompt.py
│   ├── states.py
│   └── tools.py
│
├── generated_project/   # Auto-generated projects
│
├── app.py               # Streamlit UI
├── requirements.txt
└── README.md
⚙️ Installation
1️⃣ Clone the repository
Bash
Copy code
git clone https://github.com/your-username/ai-app-builder.git
cd ai-app-builder
2️⃣ Create virtual environment
Bash
Copy code
python -m venv venv
venv\Scripts\activate  # Windows
3️⃣ Install dependencies
Bash
Copy code
pip install -r requirements.txt
4️⃣ Add environment variables
Create a .env file:
Copy code

GROQ_API_KEY=your_api_key_here
▶️ Running the App
Run Streamlit UI
Bash


Create a simple calculator web application using Flask with HTML and CSS.
The system will:
Generate project plan
Create file structure
Implement all files
Store output in generated_project/
📱 UI
Modern gradient interface
Mobile-responsive layout
Clean AI builder experience
Styled input & build button
🔐 Safety
The tool system ensures:
Files can only be written inside generated_project/
No access outside project root
Controlled command execution
🎯 Why This Project Matters
This project demonstrates:
Multi-agent AI system design
Structured output validation
Tool-based LLM execution
Workflow orchestration using LangGraph
Real-world AI product architecture
📌 Future Improvements
Add deployment automation
Add project preview feature
Add GitHub auto-push
Add Docker support
Add streaming agent responses
🧑‍💻 Author
Varsha Suresh
AI & Full Stack Developer


