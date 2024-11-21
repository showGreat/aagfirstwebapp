################ USING MODULES----- ########################
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


print(__name__)
# when you run 'function'
# __name__ is equal to __main__

# when you run 'main'
# __name__ is equal to __function__

if __name__ == "__main__":
    print('Hello')
# THE ABOVE 'IF STATEMENT' PREVENT PRINTING OF 'Hello' when you run main function.
