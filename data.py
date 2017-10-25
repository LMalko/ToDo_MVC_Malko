import time


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
                searched_expression = input("\nWhich item to modify? ")

                for line in todo_array:
                    if searched_expression in line.split(")")[0]:
                        print("Item found!", line)
                        item_found = True
                if item_found is False:
                    print("Item not found, please try again.")

            ToDoArray.choose_name_or_description(searched_expression)

    def choose_name_or_description(searched_expression):

        while True:
            user_choice = input("\nModify name or description (n/d)? ")
            if user_choice.lower() in ["n"]:
                expression_to_delete = "Change name."
                expression_to_insert = input("Write here new name: ").capitalize() + "."
                break
            elif user_choice.lower() in ["d"]:
                expression_to_delete = "Change description."
                expression_to_insert = input("Write here new description: ").capitalize() + "."
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
                    # For the purpose of displaying new item in the next loop:
                    searched_expression = expression_to_insert
                    # Break here to avoid bug when someone will insert description "is not done"/ "is done".
                    break
                elif expression_to_delete == "Change description.":
                    expression_to_delete = line.split("(", maxsplit=1)[1].split(")")[0]
                    searched_expression = expression_to_insert
                    break
                else:
                    expression_to_delete = line.split(")", maxsplit=1)[1]
        print("\nYou have modified this item: ", line, "\n\nThe changes have been recorded.\n")
        todo_array[todo_array.index(line)] = line.replace(expression_to_delete, expression_to_insert)

        with open(filename, "w", encoding="utf-8") as myfile:

            for line in todo_array:
                myfile.write(line)
                if searched_expression in line.split(")")[0]:
                    print("Now it looks like this: ", line)

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
