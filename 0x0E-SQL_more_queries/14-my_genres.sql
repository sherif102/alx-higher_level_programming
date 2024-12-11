-- use db hbtn_0d_tvshows to list all genres of Dexter
-- USE hbtn_0d_tvshows;
SELECT tg.name FROM tv_genres tg
JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
JOIN tv_shows ts ON ts.id = tsg.show_id
WHERE ts.title = 'Dexter'
ORDER BY tg.name;