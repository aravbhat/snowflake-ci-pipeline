import os
import sys
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
failures = []

# Check 1: row count — table should not be empty
cursor.execute("SELECT COUNT(*) FROM sales")
row_count = cursor.fetchone()[0]
print(f"Row count: {row_count}")
if row_count == 0:
    failures.append("Table 'sales' is empty.")

# Check 2: nulls in amount (should never be null)
cursor.execute("SELECT COUNT(*) FROM sales WHERE amount IS NULL")
null_amount_count = cursor.fetchone()[0]
print(f"Rows with NULL amount: {null_amount_count}")
if null_amount_count > 0:
    failures.append(f"{null_amount_count} row(s) have NULL amount.")

# Check 3: nulls in region (should never be null)
cursor.execute("SELECT COUNT(*) FROM sales WHERE region IS NULL")
null_region_count = cursor.fetchone()[0]
print(f"Rows with NULL region: {null_region_count}")
if null_region_count > 0:
    failures.append(f"{null_region_count} row(s) have NULL region.")

cursor.close()
conn.close()

if failures:
    print("\n❌ Data quality check FAILED:")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)   # non-zero exit code = CI step fails
else:
    print("\n✅ All data quality checks passed.")