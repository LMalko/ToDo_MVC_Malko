# ToDo_MVC_Malko

Basic ToDo app with MVC pattern.

###         1. main.py

Provides 'controller' concept of the MVC pattern. Receives input and converts it to commands
for data.py or display.py.

###         2. data.py

Provides 'model' concept of the MVC pattern. It directly manages the data, logic and rules of the application.

    @@@@    class ToDoArray()
            '''Contains the logic of ToDo items collection.'''

            Methods:
                def add_item(ToDoItem, filename='ToDo_list.txt')
                def choose_which_item_to_change(filename='ToDo_list.txt')
                def choose_name_or_description(searched_expression)
                def modify_item(searched_expression, expression_to_delete, expression_to_insert, filename='ToDo_list.txt')
                delete_item(filename='ToDo_list.txt')
                display_all(filename='ToDo_list.txt')
                display_specific_item(keyword, filename='ToDo_list.txt')
                display_done(filename='ToDo_list.txt')
                display_to_be_done(filename='ToDo_list.txt')

    @@@@    class ToDoItem(ToDoArray)
            '''Creates item instance.'''
            
            Methods:
                __init__(self, name, description, is_done=False)
                __str__(self)

###         3. display.py

Provides 'view' concept of the MVC pattern. It is an output representation of information from data.py.


