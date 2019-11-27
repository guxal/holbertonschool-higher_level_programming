-- Lists all genres of the show Dexter.
SELECT tv_genres.name
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre_id=tv_genres.id
WHERE tv_show_genres.genre_id NOT IN (SELECT tsg.genre_id FROM tv_shows AS ts INNER JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id WHERE ts.title='Dexter')
GROUP BY tv_show_genres.genre_id
ORDER BY tv_genres.name ASC
