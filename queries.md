# Sqlite Queries Reference

#### Total Play Count

```
SELECT
Plays.master_metadata_track_name,
Plays.master_metadata_album_artist_name,
Plays.master_metadata_album_album_name

FROM
    Plays


WHERE Plays.ms_played >= 20000

ORDER BY master_metadata_track_name;
```



#### Unique X Count

```
SELECT
Albums.album_name,
Songs.artist_name,
Songs.name

FROM
    Plays
    INNER JOIN Songs 
	ON Songs.spotify_track_uid = Plays.spotify_track_uid
	INNER JOIN Albums 
	ON Albums.spotify_artist_uid = Songs.spotify_artist_uid

WHERE Plays.ms_played >= 20000


GROUP BY 
  Songs.name, Songs.artist_name;
```  
 

#### Songs listened compared to release date

```
SELECT
Plays.ts,
Albums.release_date,
Albums.album_name,
Songs.artist_name,
Songs.name

FROM
    Plays
    INNER JOIN Songs 
	ON Songs.spotify_track_uid = Plays.spotify_track_uid
	INNER JOIN Albums 
	ON Albums.spotify_artist_uid = Songs.spotify_artist_uid
	
WHERE substr(Plays.ts,0,8) LIKE substr(Albums.release_date,0,8) AND Plays.ms_played >= 20000

GROUP BY 
  Songs.name, Songs.artist_name;
```



#### Songs from albums by date

```
SELECT
Albums.release_date,
Albums.album_name,
Songs.artist_name,
Songs.name


FROM
    Plays
    INNER JOIN Songs 
	ON Songs.spotify_track_uid = Plays.spotify_track_uid
	INNER JOIN Albums 
	ON Albums.spotify_artist_uid = Songs.spotify_artist_uid
	
WHERE substr(Albums.release_date,0,11)  > '2018-12-16%' AND Plays.ms_played >= 20000

GROUP BY 
  Songs.name, Songs.artist_name
  

ORDER BY 
  Albums.release_date DESC;
```

#### Songs from albums by date

`SELECT SUM(Plays.ms_played) FROM Plays;`

`SELECT SUM(Plays.ms_played) FROM Plays WHERE Plays.ms_played >= 20000;`

# Songs over x% complete
```
SELECT
Plays.ts,
Plays.master_metadata_track_name,
Plays.master_metadata_album_artist_name,
Plays.ms_played,
(Songs.duration_ms - (Songs.duration_ms * .05)) AS '95% completion',
Songs.duration_ms

FROM
    Plays
    INNER JOIN Songs 
	ON Songs.spotify_track_uid = Plays.spotify_track_uid

WHERE Plays.ms_played >= (Songs.duration_ms - (Songs.duration_ms * .05))

ORDER BY ts;
```
