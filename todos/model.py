from fastapi import Path
from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
        }

    id: int = Path(ge=1)
    item: str
    status: str

  

class TodoList(BaseModel):
    todos: List[Todo]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }