from fastapi import FastAPI
from todo import todo_router

app = FastAPI(
    title= "This is for the Todo things",
    description="Something else",
    version="1.0"
    )


app.include_router(todo_router)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)


