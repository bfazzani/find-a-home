import gui

running = True
while running:
    prefs = gui.displayWalkingBikingTransitMenu()
    print(prefs)
    running = prefs[0]
    walking_value = prefs[1]
    biking_value = prefs[2]
    transit_value = prefs[3]
    if not running:
        break

    print("walking score: {} biking score: {} transit score: {}".format(walking_value, biking_value, transit_value))
    
