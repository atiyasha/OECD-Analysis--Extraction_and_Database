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

print(str(structure_dimension))

# next step: build data base and load data, get observation array (under dimensions), also capture attributes
# create parser function


