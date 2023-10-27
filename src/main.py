import asyncio
import os
import uvicorn
from fastapi import FastAPI
from src.core.config import config
from fastapi.middleware.cors import CORSMiddleware
import json
import logging.config
from src.routers.check import router

project_root = os.path.abspath(os.path.dirname(__file__))
logging_json_path = os.path.join(project_root, '..', 'logging.json')

with open(logging_json_path, 'rt') as f:
    config_logger = json.load(f)

logging.config.dictConfig(config_logger)

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == "__main__":
    uvicorn.run('main:app', host=config.app_host, port=config.app_port, reload=config.reload)
