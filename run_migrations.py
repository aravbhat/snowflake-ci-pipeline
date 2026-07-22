import os
import glob
import snowflake.connector

conn = snowflake.connector.connect(
    account=os.environ["SNOWFLAKE_ACCOUNT"],
    user=os.environ["SNOWFLAKE_USER"],
    password=os.environ["SNOWFLAKE_PASSWORD"],
    warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
    database=os.environ["SNOWFLAKE_DATABASE"],
    schema=os.environ["SNOWFLAKE_SCHEMA"],
)

cursor = conn.cursor()

migration_files = sorted(glob.glob("migrations/*.sql"))

for filepath in migration_files:
    print(f"Running migration: {filepath}")
    with open(filepath, "r") as f:
        sql = f.read()
    for _ in conn.execute_string(sql):
        pass
  
    print(f"✅ Success: {filepath}")

cursor.close()
conn.close()
print("All migrations applied.")