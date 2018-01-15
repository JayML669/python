import datetime
import time
import math
import webbrowser

now = datetime.datetime.today()
targetTime = ''
url = 'https://youtu.be/nNpW8KZOVhw'

def waitTime(hour,minute,second, alarmHour, alarmMinute):
    totMins = ((int(alarmHour)*60) + int(alarmMinute))- ((int(hour)*60) + int(minute))
    wait= ''+str(math.floor(totMins/60))+':'+ str(totMins%60)+':'+ second
    return wait

targetTime = input('What time would you like to wake up? (ex: 06:30 or 13:57)') +':00'
target = time.strftime('%H:%M:%S')
alarmHour = targetTime[:2]
if(alarmHour[0] == '0'):
    alarmHour = alarmHour[1]
alarmMinute = targetTime[3:5]
if(alarmMinute[0] == '0'):
    alarmMinute = alarmMinute[1]

print('alarm is at', targetTime, 'and will go off in', waitTime(time.strftime('%H'),time.strftime('%M'),time.strftime('%S'),alarmHour,alarmMinute))

while(target != targetTime):
    print(time.strftime('%H:%M:%S'))
    target = time.strftime('%H:%M:%S')
    time.sleep(1)
                           
if(target == targetTime):
    print('Time to wake up')
    webbrowser.open_new(url)
                           
                
