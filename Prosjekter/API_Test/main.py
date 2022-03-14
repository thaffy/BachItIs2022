# uvicorn main:app --reload
# for å teste API i localhost...

from fastapi import FastAPI,Request
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/login")
async def login(request : Request):
    username = request.headers.get('username')
    password = request.headers.get('password')

    data = {
        'token' : 'ZWDLZHDFuDUUy8z'
    }
    return data

@app.get("/register")
async def register(request : Request):
    return{"message": "Register test"}


# @app.get("/items/{item_id}")
# async def read_item(item_id : int):
#     return {"item_id": item_id}

