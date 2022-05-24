from fastapi import FastAPI
from source.app.settings import Settings

app = FastAPI()


@app.get("/")
async def root():
    x = Settings()
    return x.database_username