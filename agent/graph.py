from pyclbr import Class

from dotenv import load_dotenv
from langchain_core.globals import set_verbose, set_debug
from langgraph.prebuilt import create_react_agent
from openai.resources.beta.threads.runs import steps

load_dotenv()
from langchain_groq import ChatGroq
from agent.prompt import *
from agent.states import *
from agent.tools import *


_ = load_dotenv()

set_debug(True)
set_verbose(True)

from langgraph.constants import END
from langgraph.graph import StateGraph, state

llm=ChatGroq(model="llama-3.3-70b-versatile",temperature=0)


user_prompt="create a simple calculator web application"
def planner_agent(state: dict) -> dict:

    user_prompt=state["user_prompt"]
    resp=llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))
    if resp is None:
        raise ValueError("planner did not return a valid response.")
    return {"plan":resp}

def architect_agent(state: dict) -> dict:
    plan: Plan =state["plan"]
    resp=llm.with_structured_output(TaskPlan).invoke(architect_prompt(plan))
    if resp is None:
        raise ValueError("architect did not return a valid response.")
    resp.plan = plan
    return {"task_plan": resp}
def coder_agent(state: dict) -> dict:
    coder_state =state.get("coder_state")
    if coder_state is None:
        coder_state = Coderstate(task_plan=state["task_plan"],current_step_idx=0)


    steps=coder_state.task_plan.implementation_steps
    if coder_state.current_step_idx>=len(steps):
        return {"coder_state":coder_state,"status":"DONE"}

    current_task=steps[coder_state.current_step_idx]
    existing_content=read_file.run(current_task.filepath)
    user_prompt=(
        f"Task: {current_task.task_description}\n"
        f"File: {current_task.filepath}\n"
        f"Existing content:\n{existing_content}\n"
        "Write the complete updated file using write_file."


    )
    system_prompt=coder_sysytem_prompt()

    coder_tools=[read_file,write_file,list_files,get_current_directory]
    react_agent=create_react_agent(llm,coder_tools)
    react_agent.invoke({"messages":[{"role":"system","content":system_prompt},
                         {"role":"user","content":user_prompt}]})

    coder_state.current_step_idx += 1
    return {"coder_state":coder_state}

1


graph =StateGraph(dict)
graph.add_node("planner",planner_agent)
graph.add_node("architect",architect_agent)
graph.add_node("coder",coder_agent)

graph.add_edge(start_key="planner",end_key="architect")
graph.add_edge(start_key="architect",end_key="coder")
graph.add_conditional_edges(
    "coder",
    lambda s:"END" if s.get("status") == "DONE" else "coder",
    {"END":END,"coder":"coder"}
)

graph.set_entry_point("planner")
agent=graph.compile()

if __name__=="__main__":
    user_prompt="create a simple calculator web application"
    result=agent.invoke({"user_prompt": user_prompt},
    {"recursion_limit":100})
    print(result)