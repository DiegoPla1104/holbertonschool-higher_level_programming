-- Only displays the rows that have a name value
SELECT score, name FROM second_table HAVING name IS NOT NULL ORDER BY score DESC;