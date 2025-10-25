# if fastapi is not installed, run: 
# pip install fastapi uvicorn
# if using uv, add it dependencies:
# uv add fastapi uvicorn

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# initialize a FastAPI application instance
app = FastAPI(title="ping")

# endpoint GET requests at the URL path "/ping"
# access it via: http://localhost:9696/ping
@app.get("/ping")
def ping():
    # return string "PONG"
    return "PONG"


class DataResponse(BaseModel):
    greeting: str;

# endpoint POST requests at the URL path "/post-ping"
# access it via: http://localhost:9696/post-ping
@app.post("/post-ping")
def postping(data: dict)    :
    result = DataResponse(greeting=f"Hello, {data['name']}!")
    return result



if __name__ == "__main__":
    # Run the FastAPI app using Uvicorn server
    # 'host="0.0.0.0"' allows external access (not just localhost)
    # 'port=9696' specifies the port number
    uvicorn.run(app, host="0.0.0.0", port=9696)

