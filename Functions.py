from xml.dom import minidom

commands = ['/lst -- Print all contacts',
            '/fln -- Find contact by last name',
            '/fph -- Find contact by phone number',
            '/add -- Add new contact to list',
            '/dlt -- Remove contact from list (by last name)',
            '/exit -- Exit from contacts list',
            '/hlp -- Print all commands']

xmldoc = minidom.parse("contact_list.xml")
contacts = xmldoc._get_firstChild()
listOfContacts = []

def addContactToList(name, lastName, phones):
    contact = {
        'name': name,
        'lastName': lastName,
        'phones': phones
    }
    listOfContacts.append(contact)


def createListFromXML():
    global listOfContacts
    listOfContacts = []
    for contact in contacts.childNodes:
        if contact.nodeType == contacts.ELEMENT_NODE:
            contactInfo = contact.childNodes
            lastName = contactInfo[3].childNodes
            name = contactInfo[1].childNodes
            phones = contactInfo[5].childNodes
            phonesList = []
            for i in range(phones.length):
                if phones[i].nodeType == contacts.ELEMENT_NODE:
                    phonesList.append(phones[i].childNodes[0].nodeValue)
            addContactToList(name[0].nodeValue, lastName[0].nodeValue, phonesList)


def printCommands():
    for command in commands:
        print command


def listContacts():
    if len(listOfContacts) == 0:
        print 'Sorry, contact list is empty.'
    else:
        printLine()
        for contact in listOfContacts:
            phones = ''
            for phone in contact['phones']:
                phones += phone + ", "
            print contact['name'] + ' ' + contact['lastName'] + ' ' + phones[:len(phones)-2]
        printLine()


def findLastName(nameToFind):
    found = False
    for contact in listOfContacts:
        if contact['lastName'] == nameToFind:
            found = True
            phones = ''
            for phone in contact['phones']:
                phones += phone + ", "
            print contact['name'] + ' ' + contact['lastName'] + ' ' + phones[:len(phones)-2]
    if not found:
        print "No matches!"


def findPhone(phoneToFind):
    found = False
    for contact in listOfContacts:
        for phone in contact['phones']:
            if phone == phoneToFind:
                found = True
                phones = ''
                for phone in contact['phones']:
                    phones += phone + ", "
                print contact['name'] + ' ' + contact['lastName'] + ' ' + phones[:len(phones)-2]
                break
    if not found:
        print "No matches!"
        
        
def addContact(inputName, inputLastName, inputPhones):
    contact = xmldoc.createElement("contact")
    nextLine = xmldoc.createTextNode('\n')
    contact.appendChild(nextLine)

    name = xmldoc.createElement("name")
    nameValue = xmldoc.createTextNode(inputName)
    name.appendChild(nameValue)

    lastName = xmldoc.createElement("lastName")
    lastNameValue = xmldoc.createTextNode(inputLastName)
    lastName.appendChild(lastNameValue)
    
    phones = xmldoc.createElement("phones")
    for i in inputPhones:
        phone = xmldoc.createElement("phone")
        phoneValue = xmldoc.createTextNode(i.replace(" ",'').replace('-',''))
        phone.appendChild(phoneValue)
        nextLine = xmldoc.createTextNode('\n  ')
        phones.appendChild(nextLine)
        addChild(phones, phone)
    addChild(contact, name)
    addChild(contact, lastName)
    addChild(contact, phones)
    
    xmldoc.childNodes[0].appendChild(contact)  # appends at end of 1st child's children
    saveXML()
    print 'Contact successfully added!'


def deleteContact(deleteLastName):
    deleted = 0
    for contact in contacts.childNodes:
        if contact.nodeType == contacts.ELEMENT_NODE:
            contactInfo = contact.childNodes
            lastName = contactInfo[3].childNodes
            if lastName[0].nodeValue == deleteLastName:
                xmldoc._get_firstChild().removeChild(contact)
                deleted += 1
    if deleted:
        saveXML()
        print "Deleted " + str(deleted) + " contact(s)."
    else:
        print "No matches found."


def refreshContacts():
    createListFromXML()


def addChild(node, child):
    nextLine = xmldoc.createTextNode('\n  ')
    node.appendChild(child)
    node.appendChild(nextLine)


def saveXML():
    file_handle = open("contact_list.xml", "w")
    xmldoc.writexml(file_handle)
    file_handle.close()


def printLine():
    print '-'*30