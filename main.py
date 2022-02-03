import webbrowser
from datetime import datetime
import time
import linecache

#get the current time
now = datetime.now()
current_time = now.strftime("%H:%M")

#choose when you want your alarm clock to ring
cand=input()

#the alarm opens the link to a song
def alarma():
    f = open("romanianaltrock", "r")
    #print(f.read())
    webbrowser.open(linecache.getline('romanianaltrock', 4))

#hour and minute of the time the alarm goes off
h=int(cand[:2])
m=int(cand[3:])

#hour and minute of the current time
hh=int(current_time[:2])
mm=int(current_time[3:])

#initialising duration(nr of minutes) between the current time and alarm time
cat=0

#calculating the duration
if(hh<h):
    cat=(h-hh)*60
else:
    if(hh>h):
        print("only future time!")
        exit()

if(mm>m & hh<h):
    cat-=60;
    cat+=60-mm+m
elif(mm>m & hh==h):
    print("only future time!")
    exit()
else:
    cat+=m-mm

#program sleeps until we reach the time set for the alarm
time.sleep(cat*60)

#when the time has passed, alarm goes off
alarma()





#ideas to expand:
#user can choose alarm or hourglass
#can choose what song genre to have the ringtone be
#each genre has a few songs in a text file
#gui
#
