import databases
import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import (
	Integer, String, DateTime, JSON, Float,
	Column, Table, MetaData,
	create_engine
)

DATABASE_URL = "sqlite:///./database.db"

db = databases.Database(DATABASE_URL)

metadata = MetaData()

fastapi_logs = Table(
    "fastapi_logs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("response_status_code", Integer),
    Column("request_method", String),
    Column("request_url", String),
    Column("request_query_params", JSON),
    Column("request_path_parameters", JSON),
    Column("timespan", Float),
    Column("created", DateTime)
)

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)