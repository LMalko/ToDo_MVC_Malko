class ToDoArray():
    '''Contains the logic of ToDo items collection.'''

    def add_item(ToDoItem, filename='ToDo_list.txt'):

        # Assign new ID to each new item by checking the length of the current collection.
        with open(filename, "r", encoding="utf-8") as myfile:
            items_ID = len(myfile.readlines()) + 1

        with open(filename, "a", encoding="utf-8") as myfile:
            myfile.write(str('{:04d}'.format(items_ID)) + " " + str(ToDoItem) + "\n")

    def check_which_item():
        pass
        modify_item(searched_expression, expression_to_delete=None, expression_to_insert=None)

    def modify_item(searched_expression,
                    filename='ToDo_list.txt',
                    expression_to_delete=None,
                    expression_to_insert=None):

        with open(filename, "r", encoding="utf-8") as myfile:
            todo_array = myfile.readlines()

        for line in todo_array:
            if searched_expression in line:
                print("You have modified this item: ", line, "The changes have been recorded.")
                # If "expression_to_delete" is not provided, the method will change the "is done" status.
                if "is not done" in line:
                    todo_array[todo_array.index(line)] = line.replace("is not done", "is done")
                elif expression_to_delete is not None and expression_to_delete in line:
                    todo_array[todo_array.index(line)] = line.replace(expression_to_delete, expression_to_insert)
                else:
                    todo_array[todo_array.index(line)] = line.replace("is done", "is not done")

        with open(filename, "w", encoding="utf-8") as myfile:
            for line in todo_array:
                myfile.write(line)

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
