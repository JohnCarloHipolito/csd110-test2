def prompt_user(init_screen):
    if init_screen:
        print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
    else:
        print("\nMENU")
    print("1. Add a record")
    print("2. Search a record")
    print("3. Update a record")
    print("4. Delete a record")
    print("5. Quit\n")

    return input("Enter your choice: ")


def add_record(pb):
    name = input("Enter name: ")
    if name in pb:
        print(f"'{name}' already existing in the phonebook.")
        return
    number = input("Enter your 10-digit phone number: ")
    if not number.isdigit() or len(number) != 10:
        print(f"You must enter a 10-digit phone number.")
        return

    pb.update({name: number})  # not casting to int, phone number starting with 0 is valid
    print("Record added.")


def search_record(pb):
    name = input("Enter name to search: ")
    if name in pb:
        print(f"{name}: {pb[name]}")
    else:
        print(f"{name} does not exist in the phonebook.")


def update_record(pb):
    name = input(f"Enter name: ")
    if name not in pb:
        print(f"'{name}' does not exist in the phonebook.")
        return
    number = input("Enter your 10-digit phone number: ")
    if not number.isdigit() or len(number) != 10:
        print(f"You must enter a 10-digit phone number.")
        return

    pb.update({name: number})
    print("Record updated.")


def delete_record(pb):
    name = input(f"Enter name: ")
    if name not in pb:
        print(f"'{name}' does not exist in the phonebook.")
    else:
        pb.pop(name)
        print("Record deleted.")


def wrong_choice():
    print("Wrong Option Entered. Please try again.")


################### Main Flow ############################
# initial screen displays "WELCOME TO THE GRANN'S PHONE DIRECTORY", succeeding shows "Menu"
initial_screen = True
phonebook = {}
# flag to quit application
quit_app = False
while not quit_app:
    choice = prompt_user(initial_screen)
    initial_screen = False

    if choice == '1':
        add_record(phonebook)
    elif choice == '2':
        search_record(phonebook)
    elif choice == '3':
        update_record(phonebook)
    elif choice == '4':
        delete_record(phonebook)
    elif choice == '5':
        quit_app = True
    else:
        wrong_choice()

