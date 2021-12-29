import sqlite3
from datetime import date, timedelta

# open db
dbfile = r".\spot_songs_py.db"
spdb = sqlite3.connect(dbfile)
cur = spdb.cursor()

# from stackoverflow
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2018, 12, 17)# 2018-12-17T13:51:56Z
end_date = date(2021, 12, 19)
all_dates_year = []

for single_date in daterange(start_date, end_date):
    #print(single_date.strftime("%Y-%m-%d"))
    all_dates_year.append(single_date.strftime("%Y-%m-%d") + "%")

days_listened = 0
empty_days = 0
no_days_list = []

for date in all_dates_year:
    cur.execute("SELECT * FROM Plays WHERE ts LIKE ? AND ms_played > 20000 ORDER BY ts ASC;",(date,))
    rows = cur.fetchall()
    if not rows:
        empty_days += 1
        no_days_list.append(date)
    else:
        days_listened += 1
        

print(start_date.strftime("%Y-%m-%d") + " - " + end_date.strftime("%Y-%m-%d"))
print("Music: " + str(days_listened))
print("No Music: " + str(empty_days))
print(no_days_list)


spdb.close()
