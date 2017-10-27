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


def ask_for_return_to_main():
    go_to_main = input("\n\nPress enter to continue")
    main()


def find_item_to_change():
    while True:
        searched_expression = input("\nWhich item needs status change? ")
        reasonable_input_minimum_length = 5
        if len(searched_expression) > reasonable_input_minimum_length:
            break
        print("\n\nToo short.")
    return searched_expression


def call_function_according_to_user_choice(user_choice):

    if user_choice == "1":
        pass_todo_item_details()
        main()

    elif user_choice == "2":
        ToDoArray.display_all()
        searched_expression = find_item_to_change()
        clear_screen()
        ToDoArray.modify_item(searched_expression, "IS NOT DONE", " IS DONE\n")
        ask_for_return_to_main()

    elif user_choice == "3":
        ToDoArray.display_all()
        searched_expression = find_item_to_change()
        clear_screen()
        ToDoArray.modify_item(searched_expression, "IS DONE", " IS NOT DONE\n")
        ask_for_return_to_main()

    elif user_choice == "4":
        clear_screen()
        ToDoArray.choose_which_item_to_change()
        ask_for_return_to_main()

    elif user_choice == "5":
        clear_screen()
        ToDoArray.delete_item()
        ask_for_return_to_main()

    elif user_choice == "6":
        clear_screen()
        keyword = find_item_to_change()
        ToDoArray.display_specific_item(keyword)
        ask_for_return_to_main()

    elif user_choice == "7":
        clear_screen()
        ToDoArray.display_all()
        ask_for_return_to_main()

    elif user_choice == "8":
        clear_screen()
        ToDoArray.display_done()
        ask_for_return_to_main()

    elif user_choice == "9":
        clear_screen()
        ToDoArray.display_to_be_done()
        ask_for_return_to_main()

    elif user_choice == "0":
        clear_screen()
        quit()


def main():

    clear_screen()
    print("\n\nToDo app \n\n")
    print_options()
    while True:
        user_choice = input("\nSelect option by number: ")
        if user_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            break
    call_function_according_to_user_choice(user_choice)


if __name__ == "__main__":
    main()
