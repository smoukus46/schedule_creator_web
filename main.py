from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/assets", StaticFiles(directory='dist/assets'), name='static')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return FileResponse("dist/index.html")


@app.get("/api/trainerList")
def get_trainers_workouts(db: Session = Depends(get_db)):
    return db.query(Trainer).all()


@app.get("/api/workoutList")
def get_workouts(db: Session = Depends(get_db)):
    return db.query(Workout).all()


@app.get("/api/get-table/{month_year}")
def get_table(month_year, db: Session = Depends(get_db)):
    if db.query(WorkoutTable).filter(WorkoutTable.month_year == month_year).first() != None:
        return db.query(WorkoutTable).filter(WorkoutTable.month_year == month_year).first()
    else:
        return JSONResponse({"message": "Расписания на такую дату не существует"})


@app.post("/api/trainerList")
def add_trainer(data=Body(), db: Session = Depends(get_db)):
     trainer = Trainer(name=data["name"])
     db.add(trainer)
     db.commit()
     db.refresh(trainer)
     return trainer

@app.post("/api/workoutList")
def add_workout(data=Body(), db: Session = Depends(get_db)):
    workout = Workout(name=data["name"])
    db.add(workout)
    db.commit()
    db.refresh(workout)
    return workout


@app.post("/api/save-table/{month_year}")
def add_workout_table_data(month_year: str, data=Body(), db: Session = Depends(get_db)):
    if db.query(WorkoutTable).filter(WorkoutTable.month_year == month_year).first() == None:
        table_data = WorkoutTable(month_year=month_year, table_data=data["rows"])
        db.add(table_data)
        db.commit()
        db.refresh(table_data)
        return table_data
    else:
        return JSONResponse(content={"message": "Расписание на такой месяц уже сущетствует"})


@app.put("/api/save-table/{month_year}")
def edit_workout_table_data(month_year: str, data=Body(), db: Session = Depends(get_db)):
    table_data = db.query(WorkoutTable).filter(WorkoutTable.month_year == month_year).first()

    table_data.table_data = data["rows"]
    db.commit()
    db.refresh(table_data)
    return table_data


@app.delete("/api/trainerList/{id}")
def delete_trainer(id, db: Session = Depends(get_db)):
    trainer = db.query(Trainer).filter(Trainer.id == id).first()

    if trainer is None:
        return JSONResponse(status_code=404, content={"message": "Trainer not found"})

    db.delete(trainer)
    db.commit()
    return trainer


@app.delete("/api/workoutList/{id}")
def delete_workout(id, db: Session = Depends(get_db)):
    workout = db.query(Workout).filter(Workout.id == id).first()

    if workout is None:
        return JSONResponse(status_code=404, content={"message": "Trainer not found"})

    db.delete(workout)
    db.commit()
    return workout
