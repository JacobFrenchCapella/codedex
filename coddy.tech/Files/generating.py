import json
# Structured data
data = {
    "title": "The White Tiger Clan's baby cotton ball",
    "genre": "Slice of life",
    "rating": 10
}
#This code will create a json file.
with open("output.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)