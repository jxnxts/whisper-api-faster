import uvicorn
import time
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import FileResponse
from routes.api import router as api_router

def create_app() -> FastAPI:
    current_app = FastAPI(title="Transcribe",
                          description="",
                          version="1.0.0", )

    current_app.include_router(api_router)
    return current_app

app = create_app()


@app.middleware("http")
async def add_process_time_header(request, call_next):
    print('inside middleware!')
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(f'{process_time:0.4f} sec')
    return response


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000,
                log_level="info", reload=True)
    print("running")