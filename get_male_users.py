from get_users import read_json
def get_male_users(data:dict)->list:
    """Gets all male users from the data
    Args:
        data (dict): The data from the JSON file
    Returns:
        list: A list of users
    """
    ans = []
    data = data['users']
    for i in data:
        if i['gender'] == "male":
            i = i['name']
            ans.append(f"{i['title']} {i['first']} {i['last']}")
    return ans

data = read_json('users.json')
print(get_male_users(data))