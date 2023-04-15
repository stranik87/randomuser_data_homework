from get_data import get_data

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    inform = []
    
    for i in data['results']:
        inform.append(i['name']['first'])
        inform.append(i['name']['last'])
        inform.append(i['phone'])
    
    return inform
    
data = get_data('randomuser_data.json')

print(get_users_data(data))