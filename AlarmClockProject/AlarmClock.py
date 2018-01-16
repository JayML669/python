import datetime
import time
import math
import webbrowser
import random
import os

now = datetime.datetime.today()
targetTime = ''
url = 'google.com'
hourToSec = 3600
minToSec = 60

if (os.path.isfile('videos.txt') == False):
    print("Error: no file found creating now...")
    createdFile = open('videos.txt', 'w')
    createdFile.write('https://youtu.be/nNpW8KZOVhw')
    createdFile.close()

def waitTime(hour,minute,second, alarmHour, alarmMinute):
    totMins = ((int(alarmHour)*60) + int(alarmMinute))- ((int(hour)*60) + int(minute))
    if(totMins>0):
        totSecs = (totMins%60)*60-int(second)
        wait= ''+str(math.floor(totMins/60))+':'+ str(math.floor(totSecs/60))+':'+ str(totSecs%60)
    elif(totMins<0):
        untilMid = (24*3600)-(int(hour)*hourToSec+int(minute)*minToSec+int(second))
        midToTarget = int(alarmHour)*hourToSec + int(alarmMinute)*minToSec
        untilTarget = untilMid+midToTarget
        wait= ''+str(math.floor(untilTarget/hourToSec))+':'+ str(math.floor(untilTarget/60)%60)+':'+ str((untilTarget%3600)%60)
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
                           
                
