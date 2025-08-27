from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello, World!"
    }

# To run the FastAPI app in development mode, use the following command:
# uvicorn app.main:app --reload --reload-dir app