from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoList


todo_router = APIRouter()

todo_list = []




@todo_router.post("/todo", response_model=Todo )
async def add_todo(todo: Todo):
    todo_list.append(todo)
    return todo  
    
    
    





@todo_router.get("/todo", response_model=TodoList)
async def retrieve_todos() -> TodoList:
    return TodoList(todos=todo_list)




@todo_router.get("/todo/{todo_id}", response_model=Todo)
async def get_single_todo(todo_id: int) -> Todo:
    for todo in todo_list:
        if todo.id == todo_id:
            return todo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exist"
    )


# responses = {200: list,
#              400: "bla... bla...",
#              401: "Noget andet bla"}


@todo_router.put("/todo/{todo_id}", response_model=Todo)
async def update_todo(todo_data: Todo, todo_id: int ) -> Todo:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            todo.status = todo_data.status
            return todo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exist"
    )



@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int):
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            del todo_list[index]
            return {"message": "Todo deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exist"
    )




@todo_router.delete("/todo")
async def delete_all_todo():
    todo_list.clear()
    return {"message": "Todos deleted successfully"}