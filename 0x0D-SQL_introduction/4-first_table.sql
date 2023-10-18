--A Script to create a table; first_table in the current database in MySQL
--first_table description:
--	id INT
--	name VARCHAR(256)
--Database name will be passed as an arg of the MySQL command
--If the table first_table already exists, your script should not fail
--You are not allowed to use the SELECT or SHOW statements

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
