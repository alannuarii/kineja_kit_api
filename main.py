import imp
from fastapi import FastAPI
from database import SessionLocal
import models
import schema


# Initialization
app = FastAPI()
db = SessionLocal()


