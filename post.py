import json
from datetime import datetime
import uuid

from find_post import find_post
from write_db import write


def create_or_update(id, created, content):
    if id == None:
        id = str(uuid.uuid4())

    with open('./data.json', 'r+') as database:
        file_data = json.load(database)
        
        existed_post = find_post(id, file_data)

        if existed_post:
            file_data["data"][file_data["data"].index(existed_post)]["content"] = content
            write(file_data)
            return

        d = {
            "id": id,
            "created": datetime.fromtimestamp(created / 1000).strftime('%d.%m.%Y %H:%M:%S'),
            "content": content,
            }

        file_data["data"].append(d)

        write(file_data)
