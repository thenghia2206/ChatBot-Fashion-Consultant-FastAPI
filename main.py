from fastapi import FastAPI
from routers import chatbotAPI
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



app.include_router(chatbotAPI.router)

# @app.get('/')
# def root_api():
#     return {"message": "Welcome to The Nghia"}

