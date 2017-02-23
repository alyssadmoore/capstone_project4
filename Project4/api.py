import zipcode, requests, foursquare


def get_keys():
    # Retrieve API keys from the keys file
    temp = ''
    with open('keys.txt', 'r') as f:
        for line in f:
            temp += line
    keys = temp.split('\n')
    return keys


def parse_foursquare_keys(keys):
    client_id = keys[0].split('=')
    client_secret = keys[1].split('=')
    keys_dict = {client_id[1], client_secret[1]}
    keys_list = list(keys_dict)
    return keys_list


def get_foursquare_names(location):
    keys = parse_foursquare_keys(get_keys())
    client_id = keys[1]
    client_secret = keys[0]
    client = foursquare.Foursquare(client_id=client_id, client_secret=client_secret)
    results = client.venues.explore(params={'near': location, 'section': 'topPicks', 'limit': '3'})
    results_list = []
    for x in range(3):
        results_list.append(results['groups'][0]['items'][x]['venue']['name'])
    return results_list

# Example response
print(get_foursquare_names("Minneapolis"))
