-- A Script which lists all records of second_table of the database hbtn_0c_0 in MySQL server.
-- Results should display both the score and the name (in this order)
-- Records should be ordered by score (top first)
-- database name is passed as an arg of mysql command

SELECT score, name FROM second_table ORDER BY score DESC;
