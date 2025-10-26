from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Hello World App")

@app.get("/hello")
def hello():
    return "Hello World"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
