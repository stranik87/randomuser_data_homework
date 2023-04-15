
from get_data import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    return len(data['results'])
data = get_data("randomuser_data.json")
get_count_users(data)


        


    