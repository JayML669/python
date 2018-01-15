import datetime
import time
import math
import webbrowser
import random

now = datetime.datetime.today()
targetTime = ''
url = 'google.com'

def waitTime(hour,minute,second, alarmHour, alarmMinute):
    totMins = ((int(alarmHour)*60) + int(alarmMinute))- ((int(hour)*60) + int(minute))
    if(totMins>0):
        wait= ''+str(math.floor(totMins/60))+':'+ str(totMins%60)+':'+ second
    elif(totMins<0):
        tempSecs = seconds
        seconds = ((1440-totMins)*60-seconds)%60
        totMins = floor(((1440-totMins)*60-tempSecs)/60)
    return wait

targetTime = input('What time would you like to wake up? (ex: 06:30 or 13:57)\n') +':00'
target = time.strftime('%H:%M:%S')
alarmHour = targetTime[:2]
if(alarmHour[0] == '0'):
    alarmHour = alarmHour[1]
alarmMinute = targetTime[3:5]
if(alarmMinute[0] == '0'):
    alarmMinute = alarmMinute[1]
    
#yn = input("Would you like to use the default video?(y/n)\n")
#if(yn == 'n'):
 #   url = input("Enter the url of the video you would like to use\n")

print('alarm is at', targetTime, 'and will go off in', waitTime(time.strftime('%H'),time.strftime('%M'),time.strftime('%S'),alarmHour,alarmMinute))

with open('videos.txt') as file:
    videos = file.readlines()

while(target != targetTime):
    print(time.strftime('%H:%M:%S'))
    target = time.strftime('%H:%M:%S')
    time.sleep(1)
                           
if(target == targetTime):
    print('Time to wake up')
    url = random.choice(videos)
    webbrowser.open_new(url)
                           
                
