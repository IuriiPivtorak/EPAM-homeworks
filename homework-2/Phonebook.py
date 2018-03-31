def menu():
    """ This function prints
    the interface options of
    the program.

    :returns: None.
    """
    print('1. Add a number')
    print('2. Remove a number')
    print('3. Lookup a number')
    print('4. Quit')
    print()

def add_contact():
    """ This function add new person
    and his/her number in the phone book.
    If name already in the dictionary,
    append the value, else create new key.

    :returns: None.
    :raises: ValueError
    """
    print("Add Name and Number")
    name = input("Name: ")
    phone = input("Number: ")
    if name in numbers.keys():
        numbers[name].append(int(phone))
    else:
        numbers[name] = [int(phone)]

def remove_contact():
    """ This function deletes contact and
    his/her number(s) from the phone book.
    If contact not in the phone book,
    prints "name was not found".

    :returns: None
    """
    print("Remove Name and Number")
    name = input("Name: ")
    if name in numbers.keys():
        numbers.pop(name)
    else:
        print(name, "was not found")


def lookup_numbers():
    """ This function shows the name
    of the contact and all his of her
    corresponding numbers.
    If contact not in the phone book,
    prints "name was not found".

    :returns: None.
    """
    name = input("Name: ")
    if name in numbers.keys():
        for i in numbers[name]:
            print(name, i)
    else:
        print(name, "was not found")

# create empty dictionary to serve
# as the phone book.
try:
    numbers
except NameError:
    numbers = {}
# print menu options for users
menu_choice = 0
menu()
# if user inputs 1, 2, or 3, corresponding functions are used,
# if input is 4, program stops,
# if input is not 1, 2, 3 or 4, print menu options again.
while menu_choice != 4:
    menu_choice = int(input("Type in a number (1-4): "))
    if menu_choice == 1:
        add_contact()
    elif menu_choice == 2:
        remove_contact()
    elif menu_choice == 3:
        lookup_numbers()
    elif menu_choice != 4:
        menu()
