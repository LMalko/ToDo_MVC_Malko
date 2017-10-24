# ToDo_MVC_Malko

Basic ToDo app with MVC pattern.

###         1. main.py

Provides 'controller' concept of the MVC pattern. Receives input and converts it to commands
for data.py or display.py.

###         2. data.py

Provides 'model' concept of the MVC pattern. It directly manages the data, logic and rules of the application.

    @@@@    class ToDoArray():
            '''Contains the logic of ToDo items collection.'''

            filename = 'ToDo_list.txt'

            Methods:
                add_item(self, filename):
                modify_item(self, filename):
                delete_item(self, filename):
                display_all(self, filename):
                display_specific_item(self, filename):
                search_for_item(keyword, filename):
                display_done(self, filename):
                display_to_be_done(self, filename):

    @@@@    class ToDoItem(AddToDo):
            '''Creates item instance.'''
            
            Methods:
                __init__(self, name, description, is_done=False):

###         3. display.py

Provides 'view' concept of the MVC pattern. It is an output representation of information from data.py.


