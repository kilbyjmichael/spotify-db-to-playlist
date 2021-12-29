import sqlite3
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# setup spotify connection
client_id = "YOURS"
client_secret = "YOURS"

token = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(auth_manager=token)

# open db
dbfile = r".\spot_songs_py.db"
spdb = sqlite3.connect(dbfile)
cur = spdb.cursor()

cur.execute("SELECT * FROM Plays WHERE total_ms_song IS NULL;")
rows = cur.fetchall()

for row in rows:
    query = sp.track(row[14])
    total_ms = query['duration_ms']
    sqls = "UPDATE Plays SET total_ms_song = ? WHERE spotify_track_uri = ?"
    inserts = (total_ms,row[14])
    cur.execute(sqls,inserts)
    spdb.commit()
    print(row[3] + "   " + str(total_ms))


spdb.close()
