-- list the number of records in the table with teh same score
SELECT score, count(score) as number FROM second_table GROUP BY score ORDER BY number DESC;