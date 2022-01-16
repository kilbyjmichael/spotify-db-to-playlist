# Spotify Stats
### DEC 17 2018 - DEC 19 2021

I've used spotify for 6 years but only had my own account since December 2018. The data in this project goes back to the join date of my current account which is used soley by me (albiet with car passengers sometimes choosing songs, but that counts because I hear them too). The data set spans 1099 days or almost exactly 3 years.

### Data Confidence 

My Sig Figs are probably horrible as this is based off of the Spotify UID and sometimes there can be songs with more than one track id. Some of these are seperate releases such as singles, but others are exactly the same to my eyes and I can't figure out why they have dupe ids. 

I have tried my best to remove these duplicates when doing queries but it's possible I have missed some so treat the small numbers as ± 3 and the big numbers as ± 10 or so.

When providing the full account data Spotify includes _all_ instances of a track play (they sent me `56,416` records, thanks Spotify!). Therefore the Plays table includes many instances of tracks played for less than 1s due to skips or other reasons. I have chosen to filter out anything played less than 20 seconds to give a more acurate representation of actual listen counts. Some records also have ms_played higher than the duration of the song which throws off some of these calcs as well.

If you see anything that doesn't add up please let me know so I can fix it.

------

### Big Numbers

+ **`2008`** unique artists played[^uniqueX]
+ **`4184`** unique albums with at least one track played[^uniqueX]
+ **`5495`** unique songs heard[^uniqueX]
+ **`39,563`** total listens (over 20s)[^playcount]

### Totals Calculations

Using these numbers we can do some fun calculations. For example if we take `2008 artists / 1099 days` we get an average of `1.8` different artists heard per day for the last 3 years. Obviously this is not a real reflection of how I listen to music, but it presents the data in a way that allows a alternative way to understand the big numbers.

+ **`1.8`** average unique artists listened per day
+ **`5.0`** average unique songs listened per day
+ **`35.999`** average songs played per day


### Song Stats (out of `5495`)

+ **`237`** (USL) unique songs listened to on day of release[^reldate]
+ **`1576`** USL to in month of release[^reldate]
+ **`3247`** USL to in year of release[^reldate]
+ **`325`**  USL from albums released before 2000[^byXdate]
+ **`4008`** USL from albums released on or after Dec 17 2018[^byXdate]


### Time Totals[^msquery]

Spotify records play time down to the millisecond! If we take a look at the sum of all records we could assume that I spent almost _an entire 24 hours_ worth of skipping songs I didn't like or back skipping songs that come after a song I like

+ Time played total dropping records below 20 seconds
  + **`6,747,764,578 ms`** or **`78.0991 days`**
  + `1874.379 hr / 1099 days` is 1.7 hours a day
+ Time played total including all records (skips, restarting plays, etc)
  + **`6,831,566,757 ms`** or **`79.0690 days`**

##### Other Time Totals (out of `39,563`) [^msx%]
+ **`15,237`** listens played 100% through
+ **`22,530`** listens played 95% through or more
+ **`23,581`** listens played 90% through or more
+ **`25,496`** listens played 80% through or more
+ **`9235`** listens played longer than 20s but less than 50%

##### Some More Time (CST)
+ **`16 days`** with no plays (over 20s)

+ List of dates with no plays:

```
2019-1-1, 2020-03-25, 2020-05-5, 2020-06-19, 2020-06-21, 2020-07-04, 2020-07-05, 2020-11-07, 2020-12-16, 2020-12-27, 2021-01-17, 2021-01-26, 2021-02-02, 2021-02-16, 2021-02-17, 2021-11-28
```
And from this list you can see that the longest stretch of using spotify was from January 2nd 2019 and March 24th 2020 or `447 days` of listening to music every day.

## Tables

#### No Play Days by Year
| 2018 (Dec)  | 2019 | 2020 | 2021 |
| :---:  | :---:  | :---:  | :---:  |
| 0 | 1  |  8 | 6 |

#### Plays per Year (CST)[^yearcount]
| 2018 (Dec)  | 2019 | 2020 | 2021 |
| :---:  | :---:  | :---:  | :---:  |
| `893` | `14018`  |  `11636` | `13016` |

#### Platform[^platform]

| Android  | Desktop | Google Home | Other |
| :---:  | :---:  | :---:  | :---:  |
| `32,211` | `2886`  |  `2485` | `1981` |


## Graphs

![fig1](https://user-images.githubusercontent.com/7111119/149645085-b92c6475-834d-4b7c-8b55-ebb416f8e669.png)

![triag1](https://user-images.githubusercontent.com/7111119/149650217-f9ef19f9-97f9-4727-a445-a2aa35ce866c.png)


[^playcount]: https://github.com/kilbyjmichael/spotify-db-to-playlist/blob/main/queries.md#total-play-count
[^reldate]: https://github.com/kilbyjmichael/spotify-db-to-playlist/blob/main/queries.md#songs-listened-compared-to-release-date
[^uniqueX]: https://github.com/kilbyjmichael/spotify-db-to-playlist/blob/main/queries.md#unique-x-count
[^byXdate]: https://github.com/kilbyjmichael/spotify-db-to-playlist/blob/main/queries.md#songs-from-albums-by-date
[^msquery]: https://github.com/kilbyjmichael/spotify-db-to-playlist/blob/main/queries.md#songs-from-albums-by-date-1
[^msx%]: https://github.com/kilbyjmichael/spotify-stats/blob/main/queries.md#songs-over-x-complete
[^platform]: https://github.com/kilbyjmichael/spotify-stats/blob/main/queries.md#platform-counting
[^yearcount]: https://github.com/kilbyjmichael/spotify-stats/blob/main/queries.md#timestamp-counting
