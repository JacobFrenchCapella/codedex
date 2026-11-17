import json
from pathlip import Path
# Structured data
data = {"status", "rank", "name"}
#Target folder and file name
folder_path = Path("codedex/coddy.tech/Files")
file_path = folder_path / "outpu1.json"
# Creates the folder (and any missing parent folders) if it doesn't exist
folder_path.mkdir(parents=True, exist_ok=True)
#This code will create a json file.
with open("output.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)