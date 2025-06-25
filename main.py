from fastapi import FastAPI, UploadFile, File, Depends
import pandas as pd
from sqlalchemy.orm import Session
from .db import init_db, SessionLocal
from .etl import process_and_store_products, compute_analytics

app = FastAPI()
init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload")
async def upload_products(file: UploadFile = File(...), db: Session = Depends(get_db)):
    df = pd.read_csv(file.file)
    process_and_store_products(df, db)
    analytics = compute_analytics(db)
    return {"message": "Data uploaded and analytics computed!", "analytics": analytics}

@app.get("/insights")
async def get_insights(db: Session = Depends(get_db)):
    analytics = compute_analytics(db)
    return analytics
