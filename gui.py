import math as m
import PySimpleGUI as sg

# print("hello world")

layout = [
    [sg.Text("Welcome to Find A Home! We can recommend you a neighborhood based upon your preferences.\n       --------------------------------------------------------------------------------------------------------------------------------")],
     [sg.Text('Please indicate how much you care about the quality of each of the following modes of transportation:')],
    # [sg.Text('Name', size=(15, 1)), sg.InputText('name')],
    # [sg.Text('Address', size=(15, 1)), sg.InputText('address')],
    # [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],
    [sg.Text("Walking:", size=(15, 1)),
     sg.Slider(range=(1, 5), default_value=3, size=(20, 15), orientation='horizontal', font=('Helvetica', 12))],
    [sg.Text("Biking:", size=(15, 1)),
     sg.Slider(range=(1, 5), default_value=3, size=(20, 15), orientation='horizontal', font=('Helvetica', 12))],
    [sg.Text("Public Transit:", size=(15, 1)),
     sg.Slider(range=(1, 5), default_value=3, size=(20, 15), orientation='horizontal', font=('Helvetica', 12))],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Simple data entry window').Layout(layout)
button, values = window.Read()

print(button, values[0], values[1], values[2])
