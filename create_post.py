import json
from datetime import datetime, timezone


def add_post_to_db(id, created, content):
    with open('./data.json', 'r+') as database:
        file_data = json.load(database)

        date = datetime.fromtimestamp(created / 1000).strftime('%d.%m.%Y %H:%M:%S')

        d = {
            "id": id,
            "created": date,
            "content": content,
            }

        file_data["data"].append(d)
        database.seek(0)
        json.dump(file_data, database, indent=2)
        