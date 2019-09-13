## Print out all of the series numbers in the JSON file
# https://realpython.com/python-requests/

import requests

response = requests.get('https://stats.oecd.org/SDMX-JSON/data/GENDER_ENT1')

if response.status_code==200:
    print('Success!')
else:
    print('An error has occurred ' + str(response.status_code))

oecd_json = response.json()

for dataSets in oecd_json:

