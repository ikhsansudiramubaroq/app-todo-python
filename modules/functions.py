# custom function dan multiple arguments
# filepath="todos.txt" merupakan default argumen yg tidak dapat diubah
def get_todos(filepath="todos.txt"):
    # documentasi code
    """ Membaca text di file todos.txt dan mengembalikan nilai vairabel
     todos_local dari list to-do item"""
    # fungsi with untuk membuka todos.txt dan fungsi r untuk read
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
# jalankan fungsi help
# print(help(get_todos))


# fungsi write todos.txt
# todos_arg adalah argument yang menampung hasil nilai dari variabel todos
def write_todos(todos_arg,filepath="todos.txt"):
    """menulis/menimpa text ke dalam file todos.txt"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

