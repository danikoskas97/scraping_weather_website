import pandas as pd
import requests
from bs4 import BeautifulSoup

# https://forecast.weather.gov/
url = 'https://forecast.weather.gov/MapClick.php?lat=34.00840430000005&lon=-118.32814719999999#.Xrhu9xP7RTY'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")
items = week.findAll(class_='tombstone-container')

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperature = [item.find(class_='temp').get_text() for item in items]
# print(period_names)
# print(short_description)
# print(temperature)
print('\n')
weather_stuff = pd.DataFrame(
    {
        'period': period_names,
        'short_description': short_description,
        'temperature': temperature,
    })
print(weather_stuff)
weather_stuff.to_csv('weather.csv')
