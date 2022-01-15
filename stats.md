# Stats DEC 17 2018 - DEC 19 2021

I've used spotify for 6 years but only had my own account since December 2018. The data in this project goes back to the join date of my current account which is used soley by me (albiet with car passengers sometimes choosing songs, but that counts because I hear them too).

##### Data Confidence 

My Sig Figs are probably horrible as this is based off of the Spotify UID and sometimes there can be songs with more than one track id. Some of these are seperate releases such as singles, but others are exactly the same to my eyes and I can't figure out why they have dupe ids. 

I have tried my best to remove these duplicates when doing queries but it's possible I have missed some so treat the small numbers as ± 3 and the big numbers as ± 10 or so.

When providing the full account data Spotify includes _all_ instances of a track play. Therefore the Plays table includes many instances of tracks played for less than 1s due to skips or other reasons. I have chosen to filter out anything played less than 20 seconds to give a more acurate representation of actual listen counts.

------

### Big Numbers

+ 2008 unique artists played[^uniqueX]

+ 4184 unique albums with at least one track played[^uniqueX]

+ 5495 unique songs heard[^uniqueX]


### Song Stats

+ 300  / 6632 songs listened to on day of release[^reldate]

+ 1896 / 6632 songs listened to in month of release[^reldate]

+ 3880 / 6632 songs listened to in year of release[^reldate]

+ 403 / 6632  songs listened from albums released before 2000[^byXdate]

+ 4777 songs listened to from albums released on or after Dec 17 2018[^byXdate]















[^reldate]: https://github.com/kilbyjmichael/spotify-db-to-playlist/blob/main/queries.md#songs-listened-compared-to-release-date
[^uniqueX]: https://github.com/kilbyjmichael/spotify-db-to-playlist/blob/main/queries.md#unique-x-count
[^byXdate]: https://github.com/kilbyjmichael/spotify-db-to-playlist/blob/main/queries.md#songs-from-albums-by-date
