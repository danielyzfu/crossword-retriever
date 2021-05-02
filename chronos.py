#Date and time manager
from datetime import date
import time

def getParsedDate():
    today = date.today()
    parsedToday = today.strftime('%y%m%d')
    return parsedToday

def getURL(date):
    url = f'https://cdn4.amuselabs.com/lat/crossword?id=tca{date}&set=latimes&embed=1&compact=1&picker=date-picker&style=1&src=https%3A%2F%2Fcdn4.amuselabs.com%2Flat%2Fdate-picker%3Fset%3Dlatimes%26style%3D1%26ads%3D0%26embed%3D1&pickerToken=eyJ1aWQiOiIyM2U5MmVkOS04M2NjLTQ1ZjctYTdiNS03ZjlkNGIwZjY5MjEiLCJ0aW1lc3RhbXAiOjE2MTIwMzczODUxOTN9'
    return url

def getDailyURL():
    return getURL(getParsedDate())

def wait(): #Slow down requests
    time.sleep(5)