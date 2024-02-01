from sqlalchemy.orm import Session
from datetime import date
from app.models import Drivers

def get_drivers(
        db: Session, 
        start_date: date, 
        end_date: date, 
        min_score: float, 
        max_score: float,  
        limit: int = 50,
        skip: int = 200 
    ):
    return db.query(Drivers).filter(
        Drivers.created_at >= start_date,
        Drivers.updated_at <= end_date,
        Drivers.driving_score >= min_score,
        Drivers.driving_score <= max_score
    ).offset(skip).limit(limit).all()
