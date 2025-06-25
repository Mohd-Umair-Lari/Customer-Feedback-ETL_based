import pandas as pd
from sqlalchemy.orm import Session
from .db import Product, Analytics

def process_and_store_products(df: pd.DataFrame, db: Session):
    # Clear old data
    db.query(Product).delete()
    db.commit()
    # Insert new data
    for _, row in df.iterrows():
        product = Product(
            id=int(row["id"]),
            name=row["name"],
            category=row["category"],
            price=float(row["price"]),
            rating=float(row["rating"])
        )
        db.add(product)
    db.commit()

def compute_analytics(db: Session):
    products = db.query(Product).all()
    if not products:
        return {}
    df = pd.DataFrame([{
        "id": p.id,
        "name": p.name,
        "category": p.category,
        "price": p.price,
        "rating": p.rating
    } for p in products])
    avg_price = df["price"].mean()
    avg_rating = df["rating"].mean()
    top_category = df["category"].mode()[0]
    # Store analytics
    db.merge(Analytics(metric="average_price", value=str(avg_price)))
    db.merge(Analytics(metric="average_rating", value=str(avg_rating)))
    db.merge(Analytics(metric="top_category", value=str(top_category)))
    db.commit()
    return {
        "average_price": round(avg_price, 2),
        "average_rating": round(avg_rating, 2),
        "top_category": top_category
    }
