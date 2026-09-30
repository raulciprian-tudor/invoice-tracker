from fastapi import FastAPI

from .clients.router import router as clients_router

app = FastAPI()
app.include_router(clients_router)


@app.get("/health", tags=["Server Status"])
async def get_status():
    return {"status": "Active"}
