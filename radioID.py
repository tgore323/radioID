import requests
import json

# ask for callsign and fetch data.
callsign = input('Please enter the desired callsign: ')
url = requests.get('https://database.radioid.net/api/dmr/user/?callsign='+callsign)
# turn JSON into text, so Python can in tern use it as dictionary
data = json.loads(url.text)

# make callsign look pretty
callsign = callsign.upper()

# Print results
print('The following ID(s) are registered to '+callsign+' : ')
for record in data['results']:
    print(record['id'], record['remarks'])
