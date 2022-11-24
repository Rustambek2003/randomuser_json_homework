from get_users import read_json
def get_users_older_than(data:dict, age:int)->list:
    """Gets all users older than a certain age from the data
    Args:
        data (dict): The data from the JSON file
        age (int): The age to filter users by
    Returns:
        list: A list of users
    """
    ans = []
    data = data['users']
    for i in data:
        if i['age'] >= age:
            i = i['name']
            ans.append(f"{i['title']} {i['first']} {i['last']}")
    return ans

data = read_json('users.json')
print(get_users_older_than(data,25))