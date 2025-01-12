import pandas as pd
import duckdb
import os

def file_to_duckdb(database:str, file_name:str, schema:str, table_name:str):
    conn = duckdb.connect(f"{database}.db")
    print(f"Connected to {database}")
    df = pd.read_csv(file_name)
    df['audit_timestamp'] = pd.Timestamp.now()
    df['audit_filename'] = file_name
    directory = os.getcwd()
    print(f"Read file {directory}/{file_name}")

    # check if schema exists
    schema_exists = conn.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.schemata WHERE schema_name = '{schema}')").fetchone()[0]
    if not schema_exists:
        conn.execute(f"CREATE SCHEMA {schema}")
        print(f"Created schema {schema}")
    else:
        print(f"Schema {schema} exists")

    conn.execute(f"CREATE OR REPLACE TABLE {schema}.{table_name} as SELECT * FROM df")

    print(f"Created {schema}.{table_name} in database {database}")
