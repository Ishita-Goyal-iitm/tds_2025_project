from fastapi import fastapi, Request

app=FastAPI()

@app.get("/")

def index () : 
    return {"message": "Welcome to the API!"}