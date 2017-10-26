from display import *
from data import *
import re
import time


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
    print("\n\nThe item was successfully created!")
    time.sleep(2)
    main()


def call_function_according_to_user_choice(user_choice):

    if user_choice == "1":
        pass_todo_item_details()
        main()
    elif user_choice == "2":
        while True:
            searched_expression = input("\nWhich item's is done? ")
            reasonable_input_minimum_length = 5
            if len(searched_expression) > reasonable_input_minimum_length:
                break
            print("\n\nToo short.")
        clear_screen()
        ToDoArray.modify_item(searched_expression, "IS NOT DONE", " IS DONE\n")
        go_to_next_screen = input("\n\nPress enter to continue")
        main()
    elif user_choice == "3":
        while True:
            searched_expression = input("\nWhich item's is not done? ")
            reasonable_input_minimum_length = 5
            if len(searched_expression) > reasonable_input_minimum_length:
                break
            print("\n\nToo short.")
        clear_screen()
        ToDoArray.modify_item(searched_expression, "IS DONE", " IS NOT DONE\n")
        go_to_next_screen = input("\n\nPress enter to continue")
        main()
    elif user_choice == "4":
        ToDoArray.choose_which_item_to_change()
        main()
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
        clear_screen()
        ToDoArray.display_all()
        go_to_next_screen = input("\n\nPress enter to continue")
        main()
    elif user_choice == "8":
        clear_screen()
        ToDoArray.display_done()
        go_to_next_screen = input("\n\nPress enter to continue")
        main()
    elif user_choice == "9":
        clear_screen()
        ToDoArray.display_to_be_done()
        go_to_next_screen = input("\n\nPress enter to continue")
        main()


def main():

    clear_screen()
    print("\n\nToDo app \n\n")
    print_options()
    while True:
        user_choice = input("\nSelect option by number: ")
        if user_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            break
    call_function_according_to_user_choice(user_choice)


if __name__ == "__main__":
    main()
