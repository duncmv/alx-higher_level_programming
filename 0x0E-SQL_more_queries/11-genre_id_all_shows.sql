-- list all shows in hbtn_0d_tvshows
-- Each record show display tv_shows.title, tv_show_genres.genre_id
-- If show doesn't have genre, display NULL
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
NATURAL JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
