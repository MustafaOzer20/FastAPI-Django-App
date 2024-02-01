import uvicorn
from fastapi.responses import JSONResponse
from fastapi import Depends, FastAPI, Query, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
from app.crud import get_drivers
from app.database import SessionLocal

from app.schemas import Records, ResponseModels
from sqlalchemy.orm import Session
from datetime import datetime



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["Content-Type"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def serialize_date(start_date, end_date):
    try:
        start = datetime.strptime(str(start_date), "%Y-%m-%d").date()
        end = datetime.strptime(str(end_date), "%Y-%m-%d").date()
        if end < start: 
            raise HTTPException(status_code=422, detail="Invalid start date or end date.")
    except:
        raise HTTPException(status_code=422, detail="Invalid start date or end date.")


@app.get("/fetch_drivers")
async def fetch_drivers(
    startDate: date = Query(..., description="Start Date (YYYY-MM-DD)"),
    endDate: date = Query(..., description="End Date (YYYY-MM-DD)"),
    minScore: float = Query(..., description="Minimum Score"),
    maxScore: float = Query(..., description="Maximum Score"),
    limit: int = Query(50, description="Limit"),
    offset: int = Query(200, description="Offset"),
    db: Session = Depends(get_db)
    ) -> ResponseModels:
    serialize_date(startDate, endDate)
    drivers = get_drivers(db, startDate, endDate, minScore, maxScore, limit, skip=offset)
    records = [
        Records(
            id=driver.id, 
            email=driver.email, 
            first_name=driver.first_name, 
            last_name=driver.last_name, 
            driving_score=driver.driving_score, 
            age=driver.age, 
            created_at=driver.created_at, 
            updated_at=driver.updated_at
        ) for driver in drivers
    ]
    response = ResponseModels(code=200, msg="Success", limit=limit, offset=offset, records=records)
    return response



@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print(f"UNHANDLED exception occured in API: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": str(exc)},
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)