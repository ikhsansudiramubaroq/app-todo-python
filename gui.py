from modules import functions
import FreeSimpleGUI as sg

sg.theme('black')

label = sg.Text("Masukkan ToDo anda")
input_box = sg.InputText(tooltip="Masukkan ToDo")
button_tambah = sg.Button("Tambah")

window = sg.Window('Aplikasi ToDo', layout=[[label],[input_box,button_tambah]])

window.read()
window.close()