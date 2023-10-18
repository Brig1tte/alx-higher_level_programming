-- The Script to compute the average score of all records in second_table of the database hbtn_0c_0 in MySQL server.
-- The result column name should be average
-- mysql is passed as database name as argument of mysql command

SELECT AVG(score) AS average FROM second_table;
