import sqlite3
from datetime import date, timedelta
from ics import Calendar, Event
import json

c = Calendar()

# open db
dbfile = r".\spot_songs_py.db"
spdb = sqlite3.connect(dbfile)
cur = spdb.cursor()

# from stackoverflow
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
# from stackoverflow
def format_timedelta(td):
    minutes, seconds = divmod(td.seconds + td.days * 86400, 60)
    hours, minutes = divmod(minutes, 60)
    return '{:02d}:{:02d}'.format(minutes, seconds)

start_date = date(2018, 12, 17)# 2018-12-17T13:51:56Z
end_date = date(2021, 12, 20) # day plus 1
all_dates_year = []

for single_date in daterange(start_date, end_date):
    #print(single_date.strftime("%Y-%m-%d"))
    all_dates_year.append(single_date.strftime("%Y-%m-%d") + "%")

days_listened = 0
empty_days = 0
no_days_list = []
cal_check = 0

for date in all_dates_year:
    cur.execute("SELECT * FROM Plays WHERE ts LIKE ? AND ms_played > 20000 ORDER BY ts ASC;",(date,))
    rows = cur.fetchall()
    print(date)
    if not rows:
        empty_days += 1
        no_days_list.append(date)
    else:
        days_listened += 1
        for row in rows:
            #print(row)
            cal_check +=1
            beg = row[0]
            sec = row[1] / 1000
            dur = timedelta(0, sec, 0)
            nam = row[3] + " - " + row[4]
            sec_listn = str(format_timedelta(timedelta(milliseconds=row[1]))) + " of " + str(format_timedelta(timedelta(milliseconds=row[2])))
            desc = "Song: " + row[3] + "\nArtist: " + row[4] + "\nAlbum: " + row[5] + "\n" + row[14] + "\n" + sec_listn
            e = Event(name=nam,begin=beg,duration=dur,description=desc)
            c.events.add(e)
        

print(start_date.strftime("%Y-%m-%d") + " - " + end_date.strftime("%Y-%m-%d"))
print("Music: " + str(days_listened))
print("No Music: " + str(empty_days))
print(no_days_list)

with open('music'+str(cal_check)+'.ics', 'w',encoding="utf-8") as f:
    f.write(str(c))

print("wrote file")
print(cal_check)
spdb.close()
