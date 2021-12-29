import sqlite3
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# setup spotify connection
# yes I know this is a bad way to do this
client_id = "YOUR_ID_HERE"
client_secret = "YOUR_SECRET_HERE"
username="YOUR_USERNAME_HERE"

token = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(auth_manager=token)

# this assumes you have a sqlite db with the json imported
dbfile = r".\spot_songs_py.db"
spdb = sqlite3.connect(dbfile)
cur = spdb.cursor()

artist = "OneRepublic"
limit = 25

# these are the default spotify data titles from their json files
cur.execute("SELECT master_metadata_track_name,spotify_track_uri,"\
            "COUNT(master_metadata_track_name) AS `pl` FROM Plays "\
            "WHERE master_metadata_album_artist_name LIKE ? "\
            "GROUP BY master_metadata_track_name ORDER BY `pl` DESC LIMIT ?;",(artist,limit))

rows = cur.fetchall()

track_ids = []

for row in rows:
    print(row)
    track_ids.append(row[1])

# must add callback uri to the app on spotify app page
token = spotipy.util.prompt_for_user_token(
    username=username,
    scope='playlist-modify-private', 
    client_id=client_id, 
    client_secret=client_secret, 
    redirect_uri="http://localhost:8888/callback")

playlist_name = artist + " Top " + str(limit)

sp1 = spotipy.Spotify(auth=token)
playlist = sp1.user_playlist_create(user=username,name=playlist_name,public=False,collaborative=False)

print(playlist['id'])

sp1.user_playlist_add_tracks(username, playlist['id'], track_ids)

spdb.close()
