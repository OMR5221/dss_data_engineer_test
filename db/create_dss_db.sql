DROP DATABASE IF EXISTS dss_db_dev;

-- Create database:
CREATE DATABASE dss_db_dev;

\c dss_db_dev;

DROP TABLE IF EXISTS dss_task1;
DROP TABLE IF EXISTS dss_task2;

CREATE TABLE task1_km (
    id serial PRIMARY KEY,
    date TIMESTAMP NOT NULL,
    page_views NUMERIC,
    visits NUMERIC,
    unique_visitors NUMERIC,
    bounce_rate NUMERIC
);

CREATE TABLE task2_products (
    id SERIAL PRIMARY KEY,
    country VARCHAR(200) NOT NULL,
    city VARCHAR(200) NOT NULL,
    product_name VARCHAR(200),
    page_views NUMERIC,
    visits NUMERIC
);

COMMIT;
