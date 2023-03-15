
def serializeDict(item) -> dict:
    if isinstance(item, dict):
        return {
            "id": str(item.get("_id")),
            "name": item.get("name"),
            "email": item.get("email"),
            "password": item.get("password"),
        }
    else:
        return {}

def serializeList(entity)->list:
    return [serializeDict(item) for item in entity]


def serializeDict(a)->dict:
    return{**{i:str(a[i]) for i in a if i=='_id'},**{i:str(a[i]) for i in a if i!='_id'}}

def serializeList(entity)->list:
    return [serializeDict(a) for a in entity]