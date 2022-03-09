import json
settings = json.load(open("./settings.json","r"))
root_path = settings['root_path']

series = json.load(open("./series.json","r"))['SECTOR_REAL']['DOM']



