import os


def print_options():

    options = ["1. Add ToDo item.", "2. Mark item as done.", "3. Mark item as not done.",
               "4. Modify item.", "5. Delete item.", "6. Search for item.", "7. Display all items.",
               "8. Display done items", "9. Display to be done items.", "0. Quit."]

    for item in options:
        print(item)


def pretty_print_table(items_details):

    print("\n\nID   NAME     (DESCRIPTION)   STATUS\n")
    for line in items_details:
        print(line)
    if items_details == []:
        print("No records found !")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
