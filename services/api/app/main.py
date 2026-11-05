import os
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import MenuItem, Order, Restaurant
from .schemas import MenuItemOut, OrderCreate, RestaurantOut

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Coimbatore Chaat API", version="0.1.0")
origins = [item.strip() for item in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",") if item.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def root():
    return {"service": "Coimbatore Chaat API", "version": "0.1.0"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/v1/restaurants", response_model=list[RestaurantOut])
def list_restaurants(db: Session = Depends(get_db)):
    return db.scalars(select(Restaurant).where(Restaurant.is_approved.is_(True))).all()

@app.get("/v1/restaurants/{restaurant_id}/menu", response_model=list[MenuItemOut])
def restaurant_menu(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = db.get(Restaurant, restaurant_id)
    if not restaurant or not restaurant.is_approved:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db.scalars(select(MenuItem).where(MenuItem.restaurant_id == restaurant_id, MenuItem.is_available.is_(True))).all()

@app.post("/v1/orders", status_code=201)
def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    order = Order(**payload.model_dump())
    db.add(order)
    db.commit()
    db.refresh(order)
    return {"id": order.id, "status": order.status, "message": "Order request recorded"}
