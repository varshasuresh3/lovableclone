import streamlit as st
from agent.graph import agent
from agent.tools import list_files, read_file

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI App Builder",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}
h1, h2, h3, h4 {
    color: #f9f9f9;
}
.stButton>button {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
}
.stTextArea textarea {
    border-radius: 12px;
}
.sidebar-title {
    font-size: 22px;
    font-weight: bold;
    color: #ffcc70;
}
.file-box {
    background-color: #1e1e1e;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("<div class='sidebar-title'>⚙️ Controls</div>", unsafe_allow_html=True)
    st.markdown("Build full apps using **natural language** ✨")
    st.divider()
    show_files = st.checkbox("📂 Show Generated Files", True)
    show_content = st.checkbox("📄 Show File Content", False)

# ---------------- HEADER ----------------
st.markdown("""
<h1 style='text-align:center;'>🤖 AI App Builder</h1>
<p style='text-align:center; font-size:18px;'>
Describe what you want — the AI builds it for you 🚀
</p>
""", unsafe_allow_html=True)

# ---------------- INPUT AREA ----------------
st.markdown("### 🧠 Your Instruction")
user_prompt = st.text_area(
    "",
    placeholder="Example: Create a simple calculator web application using HTML, CSS, and JavaScript",
    height=120
)

# ---------------- BUILD BUTTON ----------------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    build_clicked = st.button("🚀 Build My App")

# ---------------- AGENT EXECUTION ----------------
if build_clicked and user_prompt.strip():
    with st.spinner("🛠️ AI is building your application..."):
        result = agent.invoke(
            {"user_prompt": user_prompt},
            {"recursion_limit": 100}
        )
    st.success("✅ App created successfully!")

# ---------------- FILE EXPLORER ----------------
if show_files:
    st.markdown("## 📂 Generated Project Files")

    files = list_files.run(".").splitlines()
    if not files:
        st.info("No files generated yet.")
    else:
        for file in files:
            st.markdown(f"<div class='file-box'>📄 <b>{file}</b></div>", unsafe_allow_html=True)

            if show_content:
                content = read_file.run(file)
                st.code(content or "Empty file", language="python")

# ---------------- FOOTER ----------------
st.markdown("""
<hr>
<p style='text-align:center; color:#cccccc;'>
Made with ❤️ using Streamlit • LangGraph • Groq LLM
</p>
""", unsafe_allow_html=True)