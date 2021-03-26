import requests
import json


# Display menu

def get_menu_choice():
    def print_menu():
        print(' ')
        print('1. Search for user by callsign')
        print('2. Search for user by radio ID')
        print('3. Search for user by surname')
        print('4. Exit from this program')
        print(' ')

    loop = True
    int_choice = -1

    while loop:
        print_menu()
        choice = input('Enter your selection: ')

        if choice == '1':
            int_choice = 1
            loop = False
            callsign = input('Please enter the desired callsign: ')
            callsign = callsign.upper()
            try:
                url = requests.get('https://database.radioid.net/api/dmr/user/?callsign='+callsign)
                # turn JSON into text, so Python can in tern use it as dictionary
                data = json.loads(url.text)
                print('The following ID(s) are registered to '+callsign+' : ')
                for record in data['results']:
                    print(record['fname'], record['surname'], record['callsign'], record['id'], record['remarks'])
            except:
                print('Sorry, no results for '+callsign)
        elif choice == '2':
            int_choice = 2
            loop = False
            radioid = input('Please enter the desired ID: ')
            try:
                url = requests.get('https://database.radioid.net/api/dmr/user/?id='+radioid)
                # turn JSON into text, so Python can in tern use it as dictionary
                data = json.loads(url.text)
                print('The following user is registered to ID '+radioid+' : ')
                for record in data['results']:
                    print(record['fname'], record['surname'], record['callsign'], record['id'], record['remarks'])
            except:
                print('Sorry, no results for '+radioid)
        elif choice == '3':
            int_choice = 3
            loop = False
            surname = input('Please enter the desired user\'s surname: ')
            try:
                url = requests.get('https://database.radioid.net/api/dmr/user/?surname='+surname)
                # turn JSON into text, so Python can in tern use it as dictionary
                data = json.loads(url.text)
                print('The following surname is registered to '+surname+' : ')
                for record in data['results']:
                    print(record['fname'], record['surname'], record['callsign'], record['id'], record['remarks'])
            except:
                print('Sorry, no results for '+surname)
        elif choice == '4':
            int_choice = -1
            print('Exiting program... ')
            loop = False
        else:
            input('Invalid menu selection. Enter any key to try again... ')
    return [int_choice, choice]

print(get_menu_choice())

