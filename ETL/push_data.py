import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()


DB_USER = os.getenv("DB_USER")       
DB_PASSWORD = os.getenv("DB_PASSWORD")  
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")


CSV_FILE = os.getenv('CSV_FILE')   
df = pd.read_csv(CSV_FILE)

print("CSV Loaded. Shape:", df.shape)

table_name = "match_data"


df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data pushed successfully to table '{table_name}' in database '{DB_NAME}'")
