from sqlalchemy.orm import Session
from .db import models, schemas

def get_user(db: Session, user_id: str):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if user is None:
        return None
    # loc = user.location.pop(0)
    # bio = user.biometrics.pop(0)
    # location = { "latitude": loc.latitude, "longitude": loc.longitude, "altitude": loc.altitude, "heading": loc.heading}
    # biometrics = { "o2": bio.o2, "battery": bio.battery, "bpm": bio.bpm }
    # to_return = { "biometrics": biometrics, "location": location }
    return user

# def get_users(db: Session, skip: int = 0):
#     return db.query(models.Log).offset(skip).all()

def register_user(db: Session, user: schemas.UserBase):
    try:
        db_user = models.User(user)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        print("Error creating user: ", e)
        return None

# def create_user_biometrics(db: Session, user: schemas.UserCreate, biometrics: schemas.BiometricsCreate):
#     db_biometrics = models.Biometrics(user, **biometrics)
#     db.add(db_biometrics)
#     db.commit()
#     db.refresh(db_biometrics)
#     return db_biometrics

# def create_user_location(db: Session, user: schemas.UserCreate, location: schemas.LocationCreate):
#     db_location = models.Location(user, **location)
#     db.add(db_location)
#     db.commit()
#     db.refresh(db_location)
#     return db_location