import json


def add_post_to_db(id, created, content):
    with open('./data.json', 'r+') as database:
        file_data = json.load(database)
        
        d = {
            "id": id,
            "created": created,
            "content": content,
            }

        file_data["data"].append(d)
        database.seek(0)
        json.dump(file_data, database, indent=2)
        