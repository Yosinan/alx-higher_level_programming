-- a script that creates a table called first_table in the current database in MySQL server.
CREATE TABLE first_table IF NOT EXISTS (
   id INT,
   name VARCHAR(256)
)