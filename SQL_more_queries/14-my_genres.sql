-- Script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT name
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE title = "Dexter"
GROUP BY name
ORDER BY name ASC;