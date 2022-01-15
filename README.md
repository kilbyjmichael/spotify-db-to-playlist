# Spotify [Stats](stats.md) and other scripts

I requested my full listening history from Spotify this winter after seeing year after year of Spotify generated year end playlists. Regrettably, my Spotify account is only a few years old, going back to December of 2018 but I was still able to find some interesting facts out from my full listen history.

This is a work in progress, please let me know if you find errors. I'm still an SQL noob.

Queries here: [Queries Reference](queries.md)


-----

Here is DB Browser doing a query

![example_query](https://user-images.githubusercontent.com/7111119/147627345-2bd1182c-a8d7-46f1-aff8-73dadd607147.PNG)


Here is the finished playlist on Spotify

![example_list](https://user-images.githubusercontent.com/7111119/147627346-55c00d5f-45d1-4e2a-aad4-0de69eb21c33.PNG)


~~Here is the date checking script results from my data~~

This is wrong, I'm two days off because this is in GMT not Central. It's actually 18 days 2018: 0, 2019: 1, 2020: 10, 2021: 7

![musicdays](https://user-images.githubusercontent.com/7111119/147707909-3eabb0a1-4464-4f4e-9aca-e3b8ccce1bcb.PNG)


I got inspired to write the iCal script to make a more visual version. It takes the sqlite db and parses per day and creates iCal events in a file that I can import into my email. Below is that visualization. This also makes it easy to share my data to people who don't have the ability to parse through a SQLite database.


![cal](https://user-images.githubusercontent.com/7111119/147715040-d7d56606-7c42-4b9d-a294-aee5454fc511.PNG)




## References
https://towardsdatascience.com/using-python-to-create-spotify-playlists-of-the-samples-on-an-album-e3f20187ee5e
