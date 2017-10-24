class ToDoArray():
    '''Contains the logic of ToDo items collection.'''

    filename = 'ToDo_list.txt'

    def add_item(item, filename=filename):
        with open(filename, "a", encoding="utf-8") as myfile:
            myfile.write(str(item) + "\n")

    def modify_item(filename):
        pass

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

        status = "is not done."

        if self.is_done:
            status = "is done."

        return self.name + " (" + self.description + ") " + status

a = ToDoItem("wyjechać", "z dyni i z węża", True)

a.add_item()
