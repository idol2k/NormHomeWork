CREATE TABLE IF NOT EXISTS fabric(
    id SERIAL PRIMARY KEY,
    name TEXT,
    create_year INT,
    create_data INT    
);


CREATE TABLE IF NOT EXISTS workshop(
    id SERIAL PRIMARY KEY,
    id_worker INT,
    name_shop TEXT,
    cost_product INT
);

CREATE TABLE IF NOT EXISTS worker(
    id SERIAL PRIMARY KEY,
    id_workshop INT,
    product_output_per_hour INT,
    name_worker TEXT,
    experience INT,
    salary INT
);


INSERT INTO fabric(name, create_year, create_data) VALUES ('Apple', 1976, 1.04);
INSERT INTO fabric(name, create_year, create_data) VALUES ('Samsung', 1969, 13);
INSERT INTO fabric(name, create_year, create_data) VALUES ('LG', 2000, 15);


INSERT INTO workshop(id_worker, name_shop, cost_product) VALUES (1, 'phone', 2100);
INSERT INTO workshop(id_worker, name_shop, cost_product) VALUES (2, 'laptop', 3400);
INSERT INTO workshop(id_worker, name_shop, cost_product) VALUES (3, 'tv', 3400);


INSERT INTO worker(id_workshop, product_output_per_hour, name_worker, experience, salary) VALUES (1, 8, 'Serega', 4, 68);
INSERT INTO worker(id_workshop, product_output_per_hour, name_worker, experience, salary) VALUES (2, 10, 'Ignat', 5, 82);
INSERT INTO worker(id_workshop, product_output_per_hour, name_worker, experience, salary) VALUES (3, 10, 'Alex', 2, 51);


SELECT SUM(worker.product_output_per_hour * workshop.cost_product * 8) as sum_supplies_per_day FROM worker, workshop;
SELECT COUNT(product_output_per_hour) FROM worker;
JOIN workshop ON workshop.id_worker = worker.id_workshop;
GROUP BY worker.id;

 

ALTER TABLE worker ADD COLUMN age INT;
UPDATE worker SET age = 24 WHERE id = 1;
UPDATE worker SET age = 32 WHERE id = 2;
UPDATE worker SET age = 38 WHERE id = 3;