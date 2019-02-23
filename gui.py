import math as m
import PySimpleGUI as sg

# print("hello world")

#returns a tuple, (stop, walking_value, biking_value, transit_value)
def displayWalkingBikingTransitMenu():
    layout = [
        [sg.Text(
            "Welcome to Find A Home! We can recommend you a neighborhood based upon your preferences.\n       --------------------------------------------------------------------------------------------------------------------------------")],
        [sg.Text(
            'Please indicate how much you care about the quality of each of the following modes of transportation:')],
        # [sg.Text('Name', size=(15, 1)), sg.InputText('name')],
        # [sg.Text('Address', size=(15, 1)), sg.InputText('address')],
        # [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],
        [sg.Text("Walking:", size=(15, 1)),
         sg.Slider(range=(1, 5), default_value=3, size=(20, 15), orientation='horizontal', font=('Helvetica', 12))],
        [sg.Text("Biking:", size=(15, 1)),
         sg.Slider(range=(1, 5), default_value=3, size=(20, 15), orientation='horizontal', font=('Helvetica', 12))],
        [sg.Text("Public Transit:", size=(15, 1)),
         sg.Slider(range=(1, 5), default_value=3, size=(20, 15), orientation='horizontal', font=('Helvetica', 12))],
        [sg.CloseButton("Continue"), sg.Cancel()]
    ]

    window = sg.Window('Find A Home').Layout(layout)
    button, values = window.Read()

    if button == "Cancel":
        stop = True
    else:
        stop = False

    walking_value = int(values[0])
    biking_value = int(values[1])
    transit_value = int(values[2])
    vals = (stop,walking_value, biking_value, transit_value)
    return vals


#DRIVER BELOW ***************************************************
walking_value = -1
biking_value = -1
transit_value = -1

stop = False
while not stop:

    tup = displayWalkingBikingTransitMenu()
    stop = tup[0]
    walking_value = tup[1]
    biking_value = tup[2]
    transit_value = tup[3]
    if stop:
        break


    layout = [
        [sg.Text("Placeholder window. your responses:\n walking: {}   biking: {}   transit: {}".format(walking_value,
                                                                                                       biking_value,
                                                                                                       transit_value))],
        [sg.CloseButton("Close")]
    ]
    window = sg.Window("Find A Home").Layout(layout)
    button = window.Read()
    # if button == "Close":
    stop = True
    break
