# Mill Logger

A logger script for Mill heater systems. Powered by DarkSky Weather API for outside air temperature.  
This app is based on the [millheater](https://pypi.org/project/millheater/) python package

## Environment variables

This script uses python-dotenv for safely storing your environment variables.  
To make this work, create a file called `.env` and add the following keys:

```
DARKSKY_SECRET=REDACTED
MILL_USERNAME=REDACTED
MILL_PASSWORD=REDACTED
LATITUDE=REDACTED
LONGITUDE=REDACTED
```

You can obtain a darksky secret api key at [Dark Sky](https://darksky.net/dev).  
You can obtain a Mill username & password by registering in the [Millheat app](https://www.millheat.com/#millheat-app).  
Latitude and Longitude are decimal numbers. e.g. for oslo it would be 59.89 and 10.64.

## Output

The script will write data to a new CSV file called `document.csv` in the project directory.
The CSV is written with the following format: `[UNIX TIME, Outside Temp, [Rooms]]`  
Every room consists of three columns: `[RoomName, MeasuredTemperature, TargetTemperature]`  
Example data with a polling rate of 2 minutes and weather updates every 4 minutes:

```
1547550120,-2.66,Bedroom,16.0,15,Living room,18.5,23
1547550240,-2.76,Bedroom,15.0,15,Living room,18.5,23
1547550360,-2.76,Bedroom,15.0,15,Living room,18.5,23
1547550480,-2.86,Bedroom,15.0,15,Living room,18.5,23
1547550600,-2.86,Bedroom,15.0,15,Living room,18.5,23
1547550720,-2.97,Bedroom,15.0,15,Living room,18.5,23
1547550840,-2.97,Bedroom,14.0,15,Living room,18.5,23
1547550960,-3.07,Bedroom,15.0,15,Living room,18.5,23
```
