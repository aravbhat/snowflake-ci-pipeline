CREATE TABLE IF NOT EXISTS sales_db.dev.sales (
    sale_id INTEGER,
    amount NUMBER(10,2),
    region VARCHAR(50),
    currency VARCHAR(10),
    sale_date DATE
);