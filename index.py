import mill
import asyncio
import sched
import time
from datetime import datetime
import csv
import urllib.request
import json
from dotenv import load_dotenv
import os

load_dotenv()

DARKSKY_SECRET = os.getenv('DARKSKY_SECRET')
MILL_USERNAME = os.getenv('MILL_USERNAME')
MILL_PASSWORD = os.getenv('MILL_PASSWORD')
LATITUDE = os.getenv('LATITUDE')
LONGITUDE = os.getenv('LONGITUDE')

DARKSKY_URL = "https://api.darksky.net/forecast/"+DARKSKY_SECRET + \
    "/"+LATITUDE+", "+LONGITUDE+"?exclude=[hourly,daily,alerts,flags]&units=si"

mill_connection = mill.Mill(MILL_USERNAME, MILL_PASSWORD)
mill_connection.sync_connect()

current_oat = 100


def deg(num):
    return str(num)+"°C"


def getOAT():
    try:
        response = urllib.request.urlopen(DARKSKY_URL)
        data = json.load(response)
        oat = data['currently']['temperature']
        print(deg(oat))
        return oat
    except:
        print("ERROR: COULD NOT FETCH WEATHER, FALLING BACK TO LAST VALUE")
        return current_oat


current_oat = getOAT()


async def get_all_room_temps():
    await mill_connection.update_rooms()
    unixTime = int(time.time())
    currentTime = str(datetime.now()).split('.')[0]  # We don't need nanotime
    entry = [unixTime, current_oat]  # CSV Entry

    # Log current time and oat
    print(str(currentTime) + ': ' + deg(current_oat))

    rooms = mill_connection.rooms.values()
    for room in rooms:
        current_mode = room.current_mode
        target_temp = 100
        if current_mode == 1:
            target_temp = room.comfort_temp
        elif current_mode == 2:
            target_temp = room.sleep_temp
        elif current_mode == 3:
            target_temp = room.away_temp
        entry.append(room.name)
        entry.append(room.avg_temp)
        entry.append(target_temp)
        print("Room: "+room.name, "Current: " +
              deg(room.avg_temp), "Target: "+deg(target_temp))

    csvRow = (','.join(str(e) for e in entry))
    with open('document.csv', 'a') as csvFile:
        csvFile.write(csvRow+'\n')


def sync_get_all_room_temps():
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_all_room_temps())
    return loop.run_until_complete(task)


sync_get_all_room_temps()

minute = 60

delay = 1 * minute
weather_delay = 4 * minute
s = sched.scheduler(time.time, time.sleep)


def run_sync_get_all_room_temps(sc):
    s.enter(delay, 1, run_sync_get_all_room_temps, (sc,))
    sync_get_all_room_temps()


def run_getOAT(sc):
    s.enter(weather_delay, 1, run_getOAT, (sc,))
    global current_oat
    current_oat = getOAT()


s.enter(delay, 1, run_sync_get_all_room_temps, (s,))
s.enter(weather_delay, 1, run_getOAT, (s,))
s.run()
