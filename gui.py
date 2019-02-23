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
        [sg.CloseButton("Continue"), sg.CloseButton("Cancel")]
    ]

    window = sg.Window('Find A Home').Layout(layout)
    button, values = window.Read()

    running = True
    if button == "Cancel":
        running = False

    walking_value = int(values[0])
    biking_value = int(values[1])
    transit_value = int(values[2])
    vals = (running,walking_value, biking_value, transit_value)
    return vals
