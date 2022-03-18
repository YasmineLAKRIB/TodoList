from pydantic import BaseModel
# Pydantic allows auto creation of JSON Schemas from models

class Todo(BaseModel):
    title: str
    description: str 