## Print out all of the series numbers in the JSON file
# https://realpython.com/python-requests/
# https://docs.python.org/2/tutorial/datastructures.html

import requests

response = requests.get('https://stats.oecd.org/SDMX-JSON/data/GENDER_ENT1')

# validate that program is successfully receiving data
if response.status_code == 200:
    print('Success!')
else:
    print('An error has occurred ' + str(response.status_code))

oecd_json = response.json()

# array (key position) of an array (values) of dictionaries (id and name)
# structure_dimension_series captures the reference data/meta-data such as: Country name and Country code, Indicator values, Gender, and age range
structure_dimension_series = []
for series in oecd_json["structure"]["dimensions"]["series"]:
    #structure_dimension[series["keyPosition"]] = series["values"] <-- not doing this way because we want to do this manually
    structure_dimension_series.insert(series["keyPosition"], [])
    for value in series["values"]:
        value_dict = {}
        value_dict["id"] = value["id"]
        value_dict["name"] = value["name"]
        structure_dimension_series[series["keyPosition"]].append(value_dict)

# structure_dimension_observation contains all of the year values used
structure_dimension_observation = []
for observation in oecd_json["structure"]["dimensions"]["observation"]:
    for value in observation["values"]:
        structure_dimension_observation.append(int(value["id"]))

# attribute description
# investigate ternary operator
structure_attributes_series = []
for series in oecd_json["structure"]["attributes"]["series"]:
    attribute_info = {}
    if series["name"] is not None:
        attribute_info["code"] = series["name"]
    else:
        attribute_info["code"] = None

    for value in series["values"]:
        if series["name"] is not None:
            attribute_info["value"] = value["name"]
        else:
            value["name"] = None

structure_attributes_series.append(attribute_info)

for info in structure_attributes_series:
    print(str(info))
print(str(structure_dimension_observation))
print(str(structure_dimension_series[0]))
print(str(structure_dimension_series[1]))
print(str(structure_dimension_series[2]))
print(str(structure_dimension_series[3]))


# Reading line item data
series_position = []
for data_set in oecd_json["dataSets"]:
    series = data_set["series"]
    for series_key in series.keys():
        series_key_split_arr = series_key.split(':')
        #print(str(series_key_split_arr))
        country_index = int(series_key_split_arr[0])
        indicator_index = int(series_key_split_arr[1])
        gender_index = int(series_key_split_arr[2])
        age_index = int(series_key_split_arr[3])
        print(structure_dimension_series[0][country_index]["name"] + ", " + structure_dimension_series[1][indicator_index]["name"] + ", " + structure_dimension_series[2][gender_index]["name"] + ", " + structure_dimension_series[3][age_index]["name"])

        observations = series[series_key]["observations"]
        for observation_key in observations.keys():
            year = structure_dimension_observation[int(observation_key)]
            statistic = observations[observation_key][0]
            print(str(year) + " " + str(statistic))





