class ToDoArray():
    '''Contains the logic of ToDo items collection.'''

    def add_item(ToDoItem, filename='ToDo_list.txt'):

        # Assign new ID to each new item by checking the length of the current collection.
        with open(filename, "r", encoding="utf-8") as myfile:
            items_ID = len(myfile.readlines()) + 1

        with open(filename, "a", encoding="utf-8") as myfile:
            myfile.write(str('{:04d}'.format(items_ID)) + " " + str(ToDoItem) + "\n")

    def check_which_item_to_change(filename='ToDo_list.txt'):

        with open(filename, "r", encoding="utf-8") as myfile:
            todo_array = myfile.readlines()

            item_found = False
            while not item_found:
                searched_expression = input("\nWhich item to modify? ")
                for line in todo_array:
                    if searched_expression in line:
                        print("Item found!")
                        item_found = True
                if item_found is False:
                    print("Item not found, please try again.")

            ToDoArray.choose_name_or_description(searched_expression)

    def choose_name_or_description(searched_expression):

        while True:
            user_choice = input("\nModify name or description (n/d) ? ")
            if user_choice.lower() in ["n"]:
                expression_to_delete = "Change name."
                break
            elif user_choice.lower() in ["n"]:
                expression_to_delete = "Change description."
                break

        expression_to_insert = input("Write now new description: ")

        ToDoArray.modify_item(searched_expression, expression_to_delete, expression_to_insert)

    def modify_item(searched_expression,
                    expression_to_delete,
                    expression_to_insert,
                    filename='ToDo_list.txt'):

        with open(filename, "r", encoding="utf-8") as myfile:
            todo_array = myfile.readlines()

        for line in todo_array:
            if searched_expression in line:
                print("You have modified this item: ", line, "\nThe changes have been recorded.")
                todo_array[todo_array.index(line)] = line.replace(expression_to_delete, expression_to_insert)

        with open(filename, "w", encoding="utf-8") as myfile:
            for line in todo_array:
                myfile.write(line)
                if searched_expression in line:
                    print("Now it looks like this: ", line)

    def delete_item(filename):
        pass

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

        self.name = name.capitalize() + "."
        self.description = description.capitalize() + "."
        self.is_done = is_done

    def __str__(self):

        self.item_status = "is not done."

        if self.is_done:
            self.item_status = "is done."

        return self.name + " (" + self.description + ") " + self.item_status
