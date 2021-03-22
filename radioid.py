import requests
import json

# Ask for callsign, then ensure it is UPPERCASE
callsign = input('Please enter the desired callsign: ')
callsign = callsign.upper()

# Try to fetch results. If no results, then handle exception and notify user
try:
    url = requests.get('https://database.radioid.net/api/dmr/user/?callsign='+callsign)
    # turn JSON into text, so Python can in tern use it as dictionary
    data = json.loads(url.text)
    print('The following ID(s) are registered to '+callsign+' : ')
    for record in data['results']:
        print(record['id'], record['remarks'])
except:
    print('Sorry, no results for '+callsign)
