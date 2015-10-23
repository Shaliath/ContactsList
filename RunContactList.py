from Functions import *

run = True
print '-----Welcome to the Contact list!-----\n'
printCommands()
createListFromXML()
while run:
    choice = raw_input('Please, enter command: ').lower()
    if choice == '/add':
        name = raw_input('Enter the Name:').capitalize()
        lastName = raw_input('Enter the Last name:').capitalize()
        phones = raw_input('Enter the phones, separated by comma:').split(',')
        addContact(name, lastName, phones)
        refreshContacts()
    elif choice == '/dlt':
        deleteContact(raw_input('Enter Last name to delete:').capitalize())
        refreshContacts()
    elif choice == '/lst':
        listContacts()
    elif choice == '/fln':
        findLastName(raw_input('Please, enter last name: ').capitalize())
    elif choice == '/fph':
        findPhone(raw_input('Please, enter phone number: ').replace(" ",'').replace('-',''))
    elif choice == '/hlp':
        printCommands()
    elif choice == '/exit':
        run = False
    else:
        print 'You entered wrong command, try again'
