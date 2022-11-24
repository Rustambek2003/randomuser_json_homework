from get_users import read_json
def get_male_users_from_country(data:dict, country:str)->list:
    """
    Get male users from a country from the data
    Args:
        data (dict): The data from the JSON file
        country (str): The country to get users from
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
data = read_json("users.json")
count = data['users']
country = ''
for i in count:
    country += i['country'] + ' '
print(get_male_users_from_country(data,country))

    