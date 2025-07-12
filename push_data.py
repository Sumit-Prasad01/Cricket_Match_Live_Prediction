import pandas as pd
from sqlalchemy import create_engine

# --- Configurations ---
CSV_FILE_PATH = 'test.csv'   # path to uploaded file
DB_NAME = ''
DB_USER = ''
DB_PASSWORD = ''
DB_HOST = 'localhost'
DB_PORT = '5432'
TABLE_NAME = ''


df = pd.read_csv(CSV_FILE_PATH)
print("DataFrame loaded:")
print(df.head())  # only prints 5 rows for preview
print(f"Total rows loaded: {len(df)}")  # shows actual row count

# --- Step 2: Create engine ---
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# --- Step 3: Push to PostgreSQL ---
try:
    df.to_sql(TABLE_NAME, engine, index=False, if_exists='replace')  # use 'append' to keep existing data
    print(f"{len(df)} rows successfully written to table '{TABLE_NAME}' in database '{DB_NAME}'.")
except Exception as e:
    print("Error while writing to PostgreSQL:", e)