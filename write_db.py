import json


def write(data):
  with open('data.json', "w"):
    pass

  with open('data.json', "w") as database:
    json.dump(data, database, indent=2)
