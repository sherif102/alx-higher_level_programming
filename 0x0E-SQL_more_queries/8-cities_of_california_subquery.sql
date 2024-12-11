-- list the cities of california found in hbtn_0d_usa db
SELECT id, name FROM cities
WHERE cities.state_id IN (
    SELECT id FROM states
    WHERE states.name = 'California'
    )
ORDER BY id;