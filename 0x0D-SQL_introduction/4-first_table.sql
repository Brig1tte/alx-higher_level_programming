-- A Script to create a table; first_table in the current database in MySQL server
-- first_table description:
--	id INT
--	name VARCHAR(256)
-- The database name to be passed as an argument of the MySQL command
-- If the table first_table already exists, the script should not fail
-- You are not allowed to use the SELECT or SHOW statements

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
