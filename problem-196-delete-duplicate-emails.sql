-- Write your PostgreSQL query statement below
DELETE FROM Person p1 
WHERE p1.id > (
    SELECT MIN(p2.id)
    FROM Person P2
    WHERE p2.email = p1.email
);