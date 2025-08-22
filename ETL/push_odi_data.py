import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")       
DB_PASSWORD = os.getenv("DB_PASSWORD")  
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

query = """SELECT *
        FROM match_data
        WHERE format = 'ODI'
        AND batting_team IN (
    'India','Australia','England','Pakistan','New Zealand',
    'South Africa','Sri Lanka','Bangladesh','Afghanistan',
    'West Indies','Zimbabwe','Ireland','Netherlands','Scotland',
    'Nepal','Namibia','UAE','USA','Oman'
  )
  AND bowling_team IN (
    'India','Australia','England','Pakistan','New Zealand',
    'South Africa','Sri Lanka','Bangladesh','Afghanistan',
    'West Indies','Zimbabwe','Ireland','Netherlands','Scotland',
    'Nepal','Namibia','UAE','USA','Oman'
  );"""

df = pd.read_sql(query, engine)

print("ODI Data Loaded. Shape:", df.shape)

table_name = "odi_data"


df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data pushed successfully to table '{table_name}' in database '{DB_NAME}'")