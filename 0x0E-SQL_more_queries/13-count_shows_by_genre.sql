-- count all the records linked to each genre
SELECT tg.name AS genre, COUNT(tsg.genre_id) AS number_of_shows from tv_genres tg
JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;