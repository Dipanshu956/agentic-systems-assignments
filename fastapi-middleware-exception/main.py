from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


# Middleware

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print("Before request processing")
    print(f"Method: {request.method}")
    print(f"Path: {request.url.path}")

    response = await call_next(request)

    print("After response is returned")
    return response

# API Endpoint
# This endpoint will return a simple JSON response with a welcome message.

@app.get("/hello")
async def hello():
    return {
        "message": "Hello, Welcome to FastAPI!"
    }

# Custom Exception Handler
# This handler will catch any ValueError exceptions and return a custom JSON response.

@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"message": f"ValueError occurred: {str(exc)}"},
    )
# To run the application, use the command: uvicorn main:app --reload
