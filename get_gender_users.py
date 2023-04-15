from get_data import get_data

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    male = 0
    female = 0
    for user in data['results']:
        if user['gender']== 'male':
            male += 1
        elif user['gender'] == 'female':
            female += 1
    return male , female
        
data = get_data('randomuser_data.json')

print(get_gender_users(data))
    