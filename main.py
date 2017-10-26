from display import *
from data import *
import re


def pass_todo_item_details():

    while True:
        while True:
            item_name = '{:.20}'.format(input("\nProvide item's name (max 20 characters). "))
            reasonable_input_minimum_length = 3
            if len(item_name) > reasonable_input_minimum_length:
                break
            print("\n\nToo short.")
        if re.findall(r"[)(0]", item_name):
            print("Name contains one of the forbidden signs : '(', ')', '0'.")
            continue
        break

    while True:
        while True:
            item_description = '{:.150}'.format(input("\nProvide item's description (max 150 characters). "))
            reasonable_input_minimum_length = 5
            if len(item_description) > reasonable_input_minimum_length:
                break
            print("\n\nToo short.")
        if re.findall(r"[)(0]", item_description):
            print("Name contains one of the forbidden signs : '(', ')', '0'.")
            continue
        break

    new_item = ToDoItem(item_name, item_description)

    new_item.add_item()
    main()


def call_function_according_to_user_choice(user_choice):

    if user_choice == "1":
        pass_todo_item_details()
    elif user_choice == "2":
        searched_expression = input("\nWhich item's is done? ")
        ToDoArray.modify_item(searched_expression, "IS NOT DONE", " IS DONE\n")
    elif user_choice == "3":
        searched_expression = input("\nWhich item's is not done? ")
        ToDoArray.modify_item(searched_expression, "IS DONE", " IS NOT DONE\n")
    elif user_choice == "4":
        ToDoArray.choose_which_item_to_change()
    elif user_choice == "5":
        ToDoArray.delete_item()
        main()
    elif user_choice == "6":
        while True:
            keyword = input("\nWhich item You are looking for? ")
            reasonable_length = 3
            if len(keyword) > reasonable_length:
                break
            print("Too short.")
        ToDoArray.display_specific_item(keyword)
        main()
    elif user_choice == "7":
        ToDoArray.display_all()
    elif user_choice == "8":
        ToDoArray.display_done()
    elif user_choice == "9":
        ToDoArray.display_to_be_done()


def main():

    print("\n\nToDo app \n\n")
    print_options()
    while True:
        user_choice = input("\nSelect option by number: ")
        if user_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            break
    call_function_according_to_user_choice(user_choice)


if __name__ == "__main__":
    main()
