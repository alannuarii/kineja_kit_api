import imp
from fastapi import FastAPI
from database import SessionLocal
import models
import schema


# Initialization
app = FastAPI()
db = SessionLocal()


@app.get('/api/unit')
def get_all_unit():
    units = db.query(models.Unit).all()

    return units


@app.get('/api/spesifikasi')
def get_all_spesifikasi():
    spesifikasis = db.query(models.Spesifikasi).all()

    return spesifikasis


@app.get('/api/pengusahaan')
def get_all_pengusahaan():
    pengusahaans = db.query(models.Pengusahaan).all()

    return pengusahaans