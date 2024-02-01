from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from app.database import Base

class Drivers(Base):
    __tablename__ = 'driver_driver'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    first_name = Column(String)
    last_name = Column(String)
    driving_score = Column(Float)
    age = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)