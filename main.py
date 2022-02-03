import webbrowser
from datetime import datetime
import time

now = datetime.now()
current_time = now.strftime("%H:%M")
cand=input()
def alarma():
    webbrowser.open('https://www.youtube.com/watch?v=bd29sNmzaag&list=RDbd29sNmzaag&start_radio=1')
    print("Current Time =", current_time)


h=int(cand[:2])
m=int(cand[3:])

hh=int(current_time[:2])
mm=int(current_time[3:])

cat=0

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

print(cat)
time.sleep(cat*60)
alarma()