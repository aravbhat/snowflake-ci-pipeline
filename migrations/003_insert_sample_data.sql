DELETE FROM sales_db.dev.sales;

INSERT INTO sales_db.dev.sales (sale_id, amount, region, currency, sale_date)
VALUES
    (1, 250.00, 'APAC', 'USD', '2026-07-01'),
    (2, 100.50, 'EMEA', 'USD', '2026-07-02'),
    (3, 180.00, 'APAC', 'PHP', '2026-07-03'),
    (4, 75.25, 'SEA', 'INR', '2026-07-04');