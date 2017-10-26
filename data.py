import time
import re


class ToDoArray():
    '''Contains the logic of ToDo items collection.'''

    def add_item(ToDoItem, filename='ToDo_list.txt'):

        # Assign new ID to each new item by checking the length of the current collection.
        with open(filename, "r", encoding="utf-8") as myfile:
            items_ID = len(myfile.readlines()) + 1

        with open(filename, "a", encoding="utf-8") as myfile:
            myfile.write(str('{:04d}'.format(items_ID)) + " " + str(ToDoItem) + "\n")

    def choose_which_item_to_change(filename='ToDo_list.txt'):

        with open(filename, "r", encoding="utf-8") as myfile:
            todo_array = myfile.readlines()

            item_found = False
            while not item_found:
                while True:
                        searched_expression = input("\nWhich item to modify? ")
                        if len(searched_expression) > 0:
                            break
                for line in todo_array:
                    if searched_expression in line.split(")")[0]:
                        print("Item found!", line)
                        user_choice = input("Is that the one You were looking for? Y if yes, sth else to search more: ")
                        if user_choice.lower() == "y":
                            item_found = True
                            break
                        print("\nNext time be more specific.")
                if item_found is False:
                    print("\nPlease try again.")

            ToDoArray.choose_name_or_description(searched_expression)

    def choose_name_or_description(searched_expression):

        while True:
            user_choice = input("\nModify name or description (n/d)? ")
            if user_choice.lower() in ["n"]:
                expression_to_delete = "Change name."
                while True:
                    while True:
                        expression_to_insert = '{:.20}'.format(input("Write here new name: ").capitalize()) + "."
                        dot_in_input = 1
                        if len(expression_to_insert) > dot_in_input:
                            break
                    if re.findall(r"[)(0]", expression_to_insert):
                        print("Name contains one of the forbidden signs : '(', ')', '0'.")
                        continue
                    break
                break
            elif user_choice.lower() in ["d"]:
                expression_to_delete = "Change description."
                while True:
                    while True:
                        expression_to_insert = '{:.150}'.format(input("Put here new description: ").capitalize()) + "."
                        dot_in_input = 1
                        if len(expression_to_insert) > dot_in_input:
                            break
                    if re.findall(r"[)(0]", expression_to_insert):
                        print("Name contains one of the forbidden signs : '(', ')', '0'.")
                        continue
                    break
                break

        ToDoArray.modify_item(searched_expression, expression_to_delete, expression_to_insert)

    def modify_item(searched_expression,
                    expression_to_delete,
                    expression_to_insert,
                    filename='ToDo_list.txt'):

        with open(filename, "r", encoding="utf-8") as myfile:
            todo_array = myfile.readlines()

        for line in todo_array:
            if searched_expression in line.split(")")[0]:
                if expression_to_delete == "Change name.":
                    expression_to_delete = line.split(" ", maxsplit=1)[1].split("(")[0]
                    print("\nYou modified name of this item: ", line, "\n\nThe changes have been recorded.\n")
                    line_to_insert = line.replace(expression_to_delete, expression_to_insert)
                    todo_array[todo_array.index(line)] = line_to_insert
                    break
                elif expression_to_delete == "Change description.":
                    expression_to_delete = line.split("(", maxsplit=1)[1].split(")")[0]
                    print("\nYou modified description of this item: ", line, "\n\nThe changes have been recorded.\n")
                    line_to_insert = line.replace(expression_to_delete, expression_to_insert)
                    todo_array[todo_array.index(line)] = line_to_insert
                    break
                else:
                    expression_to_delete = line.split(")", maxsplit=1)[1]
                    print("\nYou modified todo status of this item: ", line, "\n\nThe changes have been recorded.\n")
                    line_to_insert = line.replace(expression_to_delete, expression_to_insert)
                    todo_array[todo_array.index(line)] = line_to_insert
                    break

        with open(filename, "w", encoding="utf-8") as myfile:

            for line in todo_array:
                myfile.write(line)                           # plus zabezpiecz kazdy input przed spacjami
            print("Now it looks like this: ", line_to_insert)

    def delete_item(filename='ToDo_list.txt'):
        with open(filename, "r", encoding="utf-8") as myfile:
            todo_array = myfile.readlines()

            while True:
                items_deleted = 0
                while True:
                    searched_expression = input("Choose item to delete: ")
                    if len(searched_expression) > 0:
                        break
                for line in todo_array:
                    if searched_expression in line.split(")")[0]:
                        print("Found it: ", line)
                        user_choice = input("Are You sure? Press Y if yes, otherwise go back to menu.")
                        items_deleted = "User changed his mind."
                        if user_choice.lower() == "y":
                            items_deleted = 1
                            todo_array[todo_array.index(line)] = "\n"
                            print("Item deleted.")
                            break
                break
            if items_deleted == 0:
                print("No such item was found.")

        with open(filename, "w", encoding="utf-8") as myfile:

            for line in todo_array:
                myfile.write(line)
            time.sleep(3)

    def display_all(filename):
        pass

    def display_specific_item(filename):
        pass

    def search_for_item(keyword, filename):
        pass

    def display_done(filename):
        pass

    def display_to_be_done(filename):
        pass


class ToDoItem(ToDoArray):
    '''Creates item instance.'''

    def __init__(self, name, description, is_done=False):

        self.name = name.lower().capitalize() + "."
        self.description = description.lower().capitalize() + "."
        self.is_done = is_done

    def __str__(self):

        self.item_status = "IS NOT DONE."

        if self.is_done:
            self.item_status = "IS DONE."

        return self.name + " (" + self.description + ") " + self.item_status
