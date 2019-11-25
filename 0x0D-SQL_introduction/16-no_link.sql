-- Show second_table except null names.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
