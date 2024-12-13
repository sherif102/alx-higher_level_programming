-- list all genres not linked to teh show 'Dexter'
SELECT name FROM tv_genres
WHERE name NOT IN (
    SELECT tg.name FROM tv_genres tg
    JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
    JOIN tv_shows ts ON ts.id = tsg.show_id
    WHERE ts.title = 'Dexter'
)
ORDER BY name;