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
The CSV is written with the following format: [UNIX TIME, Outside Temp]
Example data:

```
1547550128,-2.66,Bedroom,16.0,15,Living room,18.5,23
1547550369,-2.76,Bedroom,15.0,15,Living room,18.5,23
1547550429,-2.76,Bedroom,15.0,15,Living room,18.5,23
1547550669,-2.86,Bedroom,15.0,15,Living room,18.5,23
1547550729,-2.86,Bedroom,15.0,15,Living room,18.5,23
1547550968,-2.97,Bedroom,15.0,15,Living room,18.5,23
1547551028,-2.97,Bedroom,14.0,15,Living room,18.5,23
1547551269,-3.07,Bedroom,15.0,15,Living room,18.5,23
```
