-- list all the citi for California State
SELECT c.id, c.name
FROM states AS s 
INNER JOIN cities AS c 
ON s.id=c.state_id 
WHERE s.name = "California";  
