def find_post(id, data):
    result = [post for post in data["data"] if post["id"] == id]

    if len(result) == 0:
        return False
    
    return result[0]
    