-- lists all the cities of California
SELECT id, name FROM cities
WHERE state_id = (
    SELECT id from states
    WHERE name = 'California'
);
