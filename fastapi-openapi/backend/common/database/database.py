
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
import os
#環境変数化

import toml

try:
    toml_obj = toml.load("./sam-app/samconfig.toml")
    db_env = toml_obj.get("local")
    items = db_env.split("=")
    print(dict(items))

except:
    toml_obj = {}
print(toml_obj)
DBUSER = os.environ.get("DBUSER") or toml_obj.get("DBUSER")
DBPASSWORD = os.environ.get("DBPASSWORD") or toml_obj.get("DBPASSWORD")
DBHOST = os.environ.get("DBHOST") or toml_obj.get("DBHOST")
DBPORT = os.environ.get("DBPORT") or toml_obj.get("DBPORT")
DBNAME = os.environ.get("DBNAME") or toml_obj.get("DBNAME")
SQLALCHEMY_DATABASE_URL = "postgresql://{DBUSER}:{DBPASSWORD}@{DBHOST}:{DBPORT}/{DBNAME}"\
                    .format(
                            DBUSER=DBUSER,
                            DBPASSWORD=DBPASSWORD,
                            DBHOST=DBHOST,
                            DBPORT=DBPORT,
                            DBNAME=DBNAME
                            )

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()