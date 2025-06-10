from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI ()

app.add_middleware (
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def index (): 
    return {
        "message": "Welcome to the API!",
    }

@app.get ("/api/params")
def search (request: Request):
    parameters = list ()
    parameter_values = list ()

    for parameter_name in request.query_params.keys ():

        parameter_values = request.query_params.getlist (parameter_name)
        for values in parameter_values:
            parameters.append ({
                "name": parameter_name,
                "value": values
            })
        
    print(parameters)        

    return {
        "parameters": parameters,
    }