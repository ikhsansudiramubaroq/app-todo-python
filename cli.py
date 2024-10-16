# import function.py di folder modules
from modules import  functions
import time

# fungsi import time menggunakan strftime
now = time.strftime("%b %d, %Y %H:%M:%S")
print("Waktu sekarang", now)

while True:
    # user aksi berisi input menu
    user_action = input("ketik tambah, tampil, edit, hapus atau keluar: ")
    # menghilangkan string ketik user menambahkan spasi
    user_action = user_action.strip()

    # startswith berfungsi ketika user input edit/tambah maka yg dijalankan adalah input 'tambah'
    if user_action.startswith("tambah"):
        # fungsi ketika user input 'tambah' maka tambah tidak akan dimasukkan ke dalam list
        # fungsi [7:] merupakan str 'tambah' dihitung mulai dari 0
        todo = user_action[7:]

        # menggunakan custom function get_todos dan default argument 'filepath'
        todos = functions.get_todos()

        # menambahkan inputtodo kedalam list
        todos.append(todo + '\n')

        # memanggil function write_todos dan menambahkan variabel todos
        # serta menggunakan default arg 'filepath'
        functions.write_todos(todos)

        # case ketika user input 'tampil' dan operator bitwise menggunaan tanda | menghasilkan true
    elif user_action.startswith("tampil"):

        # menggunakan custom function get_todos
        todos = functions.get_todos()

        # pengulangan for untuk menghilangkan kutip dan kurung pada list dan memberikan nomer
        # menggunakan fungsi index dan enumerate
        for index, item in enumerate(todos):
            # fungsi variabel item untuk menghilangkan \n
            item = item.strip('\n')
            # fungsi titte untuk huruf pertama menjadi kapital
            # item = item.title() - cara ke 1
            row = f"{index + 1}-{item}"
            print(row)

    # fungsi edit
    elif user_action.startswith("edit"):
        # program mencoba menjalankanfungsi dibawah nya ketika error akan menjalankan except
        try:
            # merubah tipe data str ke int
            number= int(user_action[5:])
            print(number)
            # mengurangi list index karena python dimulai dari 0
            number = number - 1

            # menggunakan custom function get_todos
            todos = functions.get_todos()

            new_todo = input("Masukkan todo baru : ")
            # mengambil nomer todos dalam list indexing dan melakukan replace untuk menu edit
            todos[number] = new_todo + '\n'

            # memanggil function write_todos dan menambahkan variabel todos
            functions.write_todos(todos)
        except ValueError:
            print("Perintah yang anda masukkan salah")
            # fungsi continu melanjutkan code program dari atas dan menjalankan nya
            continue

    # fungsi untuk menghapus isi dari list
    elif user_action.startswith("hapus"):
        try:
            number = int(user_action[6:])

            # menggunakan custom function get_todos dan default arg 'filepath'
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            # fungsi pop untuk menghapus
            todos.pop(index)

            # memanggil function write_todos dan menambahkan variabel todos
            functions.write_todos(todos)
            pesan = f"Todo {todo_to_remove} berhasil dihapus dari daftar"
            print(pesan)
        # error ketika user input nomer untuk dihapus tetapi tidak tersedia dalam list
        except IndexError:
            print("Nomer yang anda masukkan tidak ada")
            continue

    # case ketika user input 'keluar'
    elif user_action.startswith("keluar"):
        break

    # case ketika user input tidak sesuai dengan menu user_action
    else:
        print("Tidak ada menu yang bisa ditampilkan")

print("Bye!")