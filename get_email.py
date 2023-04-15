import json
from get_data import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    lst = [] 
    for user in data['results']:
        lst.append(user['email'])
    
    
    
    return lst
data = get_data("randomuser_data.json")
print(get_email(data))
    