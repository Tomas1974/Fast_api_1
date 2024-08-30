from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item  # This expects an Item object, not a string

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": {
                    "item": "Example task",
                    "status": "incomplete"
                }
            }
        }

# Explanation of Config options:
# schema_extra: Provides an example of how the Todo model can be structured. This is helpful for documentation purposes, making it clear what kind of data the model expects.
# orm_mode: Allows the Pydantic model to interact seamlessly with ORM models (like those from SQLAlchemy). This is particularly useful in web frameworks when fetching data from a database and returning it in a Pydantic model format.
# extra = 'forbid': Configures the model to raise an error if any extra fields are included in the input data that are not defined in the model schema.

class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

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