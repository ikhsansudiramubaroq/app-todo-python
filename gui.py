# import function dari folder module
from modules import functions
# import freesimplegui
import FreeSimpleGUI as sg

# tema warna aplikasi todo
sg.theme('black')

# untuk label tex
label = sg.Text("Masukkan ToDo anda")
# input box
input_box = sg.InputText(tooltip="Masukkan ToDo", key="todo")
# button
button_tambah = sg.Button("Tambah")

# window aplikasi atau tampilan keseluruhan
window = sg.Window('Aplikasi ToDo',
                   layout=[[label],[input_box,button_tambah]],
                   font=('Helvetica', 14))

# fungsi looping menggunakan while
while True:
    # event=button"tambah", value=keytodo'
    event, values = window.read()
    print(event)
    print(values)
    # kondisi event=button yang di klik
    match event:
        # jika button tambah yg ditekan fungsi dijalankan
        case "Tambah":
            # untuk mengambil fungsi get_todos berisi 'r' pada function
            todos = functions.get_todos()
            # key berisitodo pada input box yaitu values
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            # untuk mengambil fungsi write_todos berisi 'w' pada function
            functions.write_todos(todos)
        # fungsi menutup window agar tidak error
        case sg.WIN_CLOSED:
            break

window.close()