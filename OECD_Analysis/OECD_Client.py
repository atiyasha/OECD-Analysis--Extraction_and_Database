## Print out all of the series numbers in the JSON file
# https://realpython.com/python-requests/
# https://docs.python.org/2/tutorial/datastructures.html

import requests

response = requests.get('https://stats.oecd.org/SDMX-JSON/data/GENDER_ENT1')

if response.status_code==200:
    print('Success!')
else:
    print('An error has occurred ' + str(response.status_code))

oecd_json = response.json()

for data_set in oecd_json["dataSets"]:
    series = data_set["series"]
    for series_key in series.keys():
        print(series_key)

# array (key position) of an array (values) of dictionaries (id and name)

structure_dimension= []
for series in oecd_json["structure"]["dimensions"]["series"]:
    #structure_dimension[series["keyPosition"]] = series["values"] <-- not doing this way because we want to do this manually
    structure_dimension.insert(series["keyPosition"], [])
    for value in series["values"]:
        value_dict = {}
        value_dict["id"] = value["id"]
        value_dict["name"] = value["name"]
        structure_dimension[series["keyPosition"]].append(value_dict)

print(str(structure_dimension[0]))
print(str(structure_dimension[1]))
print(str(structure_dimension[2]))
print(str(structure_dimension[3]))
