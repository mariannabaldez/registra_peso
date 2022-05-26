from fastapi import FastAPI
from source.app.settings import Settings
from app.routers.api import router


app = FastAPI()


@app.get("/")
async def root():
    x = Settings()
    return x.database_username

#conectar e desconectar bd
