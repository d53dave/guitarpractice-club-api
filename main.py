import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.logger import logger as fastapi_logger
from logging.config import dictConfig

from routers import exercises
from config import Settings

with open("log.conf.json") as json_file:
    dictConfig(json.loads(json_file.read()))

settings = Settings()

app = FastAPI()

origins = [
    'guitarpractice-club-app-git-develop.brever.vercel.app',
    'guitarpractice.club', '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    exercises.router,
    prefix="/api/v1/exercises",
    tags=['forms'],
)


@app.get("/documentation", tags=["documentation"])
async def get_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


fastapi_logger.info("Application startup")
