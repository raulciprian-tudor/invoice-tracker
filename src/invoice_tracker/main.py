from fastapi import FastAPI

from .clients import router

app = FastAPI()

app.include_router(router.client)


@app.get("/health", tags=["Server Status"])
async def get_status():
    return {"status": "Active"}
