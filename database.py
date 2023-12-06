from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import psycopg2
from psycopg2.extras import RealDictCursor
from config import setting

SQLALCHEMY_DATABASE_URL = f"postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}"
print(setting)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SeesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SeesionLocal()
    try:
        yield db
    finally:
        db.close()


while True:
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="postgres",
            password="Mobiledev1307",
            cursor_factory=RealDictCursor,
        )
        print("Connect database successfully")
        break
    except Exception as ex:
        print(f"Connection database failed {ex}")
        time.sleep(2)
