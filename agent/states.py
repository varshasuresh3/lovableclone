from typing import Optional

from pydantic import BaseModel,Field,ConfigDict

class File(BaseModel):
    path: str= Field(description="the path of the file to be created or modified")
    purpose: str= Field(description="the purpose of the file,e.g.'main application logic','data processing module',etc.")


class Plan(BaseModel):
    name: str=Field(description="the name of the app to build")
    description: str = Field(
        description="a one line description of the app to built,e.g. 'A web application for managing personal finance")
    techstack: str = Field(
        description="the tech stack to be used for the app,e.g. 'python','javascript','react','flask',etc")
    features: str = Field(
        description="the features of the app should have,e.g. 'user authentication','data visualization',etc)")
    files:list[File]=Field(
        description="a list of files to be created,each with a 'path' and 'purpose'")

class ImplementationTask(BaseModel):
    filepath: str= Field(description="the path of the file to be modified")
    task_description: str= Field(description="a detailed description of the task to be performed on the file, e.g.'add user',etc")

class TaskPlan(BaseModel):
    implementation_steps: list[ImplementationTask]= Field(description="the list of steps to be taken to implement the task")
    model_config = ConfigDict(extra="allow")

class Coderstate(BaseModel):
    task_plan:TaskPlan=Field(description="the plan for the task to be implemented")
    current_step_idx:int=Field(0,description="the index of the current step in the implementation steps")
    current_file_content:Optional[str]=Field(None,description="the content of the file currently being edited or created")