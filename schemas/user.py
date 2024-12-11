def userEntiry(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"],
        # "created_at": item["created_at"],
        # "updated_at": item["updated_at"],
    }


def usersEntity(entity) -> list:
    return [userEntiry(item) for item in entity]