from display import *
from data import *


def add_todo_item():

    item_name = '{:.20}'.format(input("\nProvide item's name (max 20 characters). "))
    item_description = '{:.150}'.format(input("\nProvide item's description (max 150 characters)."))

    while True:
        item_is_done = input("\nHas item been done already (y/n)? ")
        if item_is_done == "y":
            new_item = ToDoItem(item_name, item_description, True)
            break
        if item_is_done == "n":
            new_item = ToDoItem(item_name, item_description)
            break

    new_item.add_item()
    main()


def act_according_to_user_choice(user_choice):

    if user_choice == "1":
        add_todo_item()
    if user_choice == "2" or user_choice == "3":
        searched_expression = input("Which item's status changed? ")
        ToDoArray.modify_item(searched_expression)


def print_options():

    options = ["1. Add ToDo item.", "2. Mark item as done.", "3. Mark item as not done.",
               "4. Delete item.", "5. Modify item.", "6. Search for item.", "7. Display all items."]

    for item in options:
        print(item)


def main():

    print("\n\nToDo app \n\n")
    print_options()
    while True:
        user_choice = input("\nSelect option by number: ")
        if user_choice in ["1", "2", "3"]:
            break
    act_according_to_user_choice(user_choice)


if __name__ == "__main__":
    main()
