from sqlalchemy.orm import Session
from datetime import date
from app import models, schemas


def get_drivers(
        db: Session, 
        start_date: date, 
        end_date: date, 
        min_score: float, 
        max_score: float,  
        limit: int = 50,
        skip: int = 200 
    ):
    return db.query(models.Drivers).offset(skip).limit(limit).all()
