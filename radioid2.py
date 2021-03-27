import requests
import json
print(' ')
print(50 * '=')
print('RadioID v2 by Tim Gore, KE6QBV')
print(50 * '=')

def get_menu_choice():
    ''' Gets the users choice from the below menu '''
    def print_menu():
        ''' Prints the actual menu '''
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
            #loop = False
            callsign = input('\nPlease enter the desired callsign: ')
            callsign = callsign.upper()
            try:
                url = requests.get('https://database.radioid.net/api/dmr/user/?callsign='+callsign)
                data = json.loads(url.text)
                print('\nThe following ID(s) are registered to '+callsign+' :')
                for record in data['results']:
                    print(record['fname'], record['surname'], record['callsign'], record['id'], record['remarks'])
                input('\nPress ENTER to return to the main menu.')
            except:
                print('\nSorry, no results for '+callsign)
                input('\nPress ENTER to return to the main menu.')
        elif choice == '2':
            int_choice = 2
            #loop = False
            radioid = input('\nPlease enter the desired ID: ')
            try:
                url = requests.get('https://database.radioid.net/api/dmr/user/?id='+radioid)
                data = json.loads(url.text)
                print('\nThe following user is registered to ID '+radioid+' : \n')
                for record in data['results']:
                    print(record['fname'], record['surname'], record['callsign'], record['id'], record['remarks'])
                input('\nPress ENTER to return to the main menu.')
            except:
                print('\nSorry, no results for '+radioid+'')
                input('\nPress ENTER to return to the main menu.')
        elif choice == '3':
            int_choice = 3
            #loop = False
            surname = input('\nPlease enter the desired user\'s surname: ')
            try:
                url = requests.get('https://database.radioid.net/api/dmr/user/?surname='+surname)
                data = json.loads(url.text)
                print('\nThe following surname is registered to '+surname+' : ')
                for record in data['results']:
                    print(record['fname'], record['surname'], record['callsign'], record['id'], record['remarks'])
                input('\nPress ENTER to return to the main menu.')
            except:
                print('\nSorry, no results for '+surname)
                input('\nPress ENTER to return to the main menu.')
        elif choice == '4':
            int_choice = -1
            print('\nExiting program...\n')
            loop = False
        else:
            input('\nInvalid menu selection. Press ENTER to go back... ')
    #return #[int_choice, choice]

print(get_menu_choice())
