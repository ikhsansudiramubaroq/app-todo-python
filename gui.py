# import function dari folder module
from modules import functions
# import freesimplegui
import FreeSimpleGUI as sg

# tema warna aplikasitodo
sg.theme('black')

# untuk label text
label = sg.Text("Masukkan ToDo anda")
# input box
input_box = sg.InputText(tooltip="Masukkan ToDo", key="todo")
# button
button_tambah = sg.Button("Tambah")
button_edit = sg.Button("Edit")
button_hapus = sg.Button("Hapus")
button_keluar = sg.Button("Keluar")

# untuk menampilkan daftartodo yang ada pada todos.txt
listbox_todos = sg.Listbox(values=functions.get_todos(),
                           key='list_todos',
                           enable_events=True,
                           size=(40, 10))

# window aplikasi atau tampilan keseluruhan
window = sg.Window('Aplikasi ToDo',
                   layout=[[label],
                           [input_box, button_tambah, button_edit, button_hapus],
                           [listbox_todos],
                           [button_keluar]],
                   font=('Helvetica', 14))

# fungsi looping menggunakan while
while True:
    # membaca event dan values
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
            # update listbox_todos setelah penambahan
            window['list_todos'].update(values=todos)
        # jika button edit yg ditekan fungsi dijalankan
        case "Edit":
            try:
                # ambil daftar todos yang ada
                todos = functions.get_todos()
                # cek apakah ada item yang dipilih
                selected_todo = values['list_todos'][0]
                # gantitodo yang dipilih
                new_todo = sg.popup_get_text("Edit ToDo", default_text=selected_todo.strip())
                if new_todo:
                    index = todos.index(selected_todo)
                    todos[index] = new_todo + "\n"
                    functions.write_todos(todos)
                    # update listbox_todos setelah pengeditan
                    window['list_todos'].update(values=todos)
            except IndexError:
                sg.popup("Pilih ToDo yang ingin diedit")
        # jika button hapus yg ditekan fungsi dijalankan
        case "Hapus":
            try:
                # ambil daftar todos yang ada
                todos = functions.get_todos()
                # cek apakah ada item yang dipilih
                selected_todo = values['list_todos'][0]
                # hapustodo dari daftar
                todos.remove(selected_todo)
                # tulis kembali daftar todos ke file
                functions.write_todos(todos)
                # update listbox_todos setelah penghapusan
                window['list_todos'].update(values=todos)
            except IndexError:
                sg.popup("Pilih ToDo yang ingin dihapus")
        # jika button keluar yg ditekan, keluar dari aplikasi
        case "Keluar":
            break
        # jika item pada listbox diklik
        case 'list_todos':
            # menampilkantodo yang dipilih ke dalam input box
            window['todo'].update(value=values['list_todos'][0].strip())
        # fungsi menutup window agar tidak error
        case sg.WIN_CLOSED:
            break

window.close()
