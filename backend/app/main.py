from fastapi import FastAPI
from sqlalchemy import text

from backend.app.core.database import engine


app = FastAPI(title="AlgoLab API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/health/db")
async def database_health_check():
    async with engine.connect() as connection:
        result = await connection.execute(text("SELECT 1"))
        return {"database": result.scalar_one()}