from typing import Annotated
import uvicorn
from fastapi.responses import JSONResponse
from fastapi import Depends, FastAPI, Query, Form, HTTPException, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
from app.crud import get_drivers
from app.database import SessionLocal

from app.schemas import ResponseModels
from app import models
from sqlalchemy.orm import Session


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


@app.get("/process_data")
async def process_data(
    start_date: date = Query(..., description="Start Date (YYYY-MM-DD)"),
    end_date: date = Query(..., description="End Date (YYYY-MM-DD)"),
    minScore: float = Query(..., description="Minimum Score"),
    maxScore: float = Query(..., description="Maximum Score"),
    limit: int = Query(50, description="Limit"),
    offset: int = Query(200, description="Offset"),
    db: Session = Depends(get_db)
    ) -> ResponseModels:
    drivers = get_drivers(db, start_date, end_date, minScore, maxScore, limit, skip=offset)
    print(drivers)
    # query_params nesnesini kullanarak gelen verileri işleyebilirsiniz
    return {"message": "Data processed successfully"}



@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print(f"UNHANDLED exception occured in API: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": str(exc)},
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)