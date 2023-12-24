import _mysql_connector
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, String, MetaData, Table

host = "sql12.freesqldatabase.com"
database_name = "sql12671479"
user = "sql12671479"
password = "jcVXxlPEcP"
port = 3306

# Create the SQLAlchemy engine
DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database_name}"
engine = create_engine(DATABASE_URL)


DATABASE_URL = "mysql+mysqlconnector://sql12671479:jcVXxlPEcP@sql12.freesqldatabase.com:3306/sql12671479"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
app = FastAPI()
# Replace "TABLE 1" and "your_column_name" with the actual table and column names
your_table = Table(
    "TABLE 1",
       metadata,
    Column("Dependents", String),
)

@app.get("/distinct-values/")
async def get_distinct_values():
    try:
        with engine.connect() as connection:
            query = your_table.select().distinct(your_table.c.Dependents)
            result = connection.execute(query)
            distinct_values = [row.Dependents for row in result]

        return {"distinct_values": distinct_values}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))