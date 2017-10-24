class AddToDo():
    '''Contains the logic of ToDo list.'''

    def add_item(self, filename):
        pass

    def modify_item(self, filename):
        pass

    def delete_item(self, filename):
        pass

    def display_all(self, filename):
        pass

    def display_specific_item(self, filename):
        pass

    def search_for_item(keyword, filename):
        pass

    def display_done(self, filename):
        pass

    def display_to_be_done(self, filename):
        pass


class ToDoItem(AddToDo):
    '''Creates item instance.'''

    def __init__(self, name, description, is_done=False):
        pass
