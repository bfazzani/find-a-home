import googleMaps as maps
import gui
import walkScore as ws

address = "plano east senior high school"
adData = maps.getCoordFromAddress(address)
transitScores = ws.getTransitScores(adData[0], adData[1], adData[2])
print("{ad} at lat:{lat} lng:{lng}".format(ad=adData[0], lat=adData[1], lng=adData[2]))
print(transitScores)

running = True
while running:
    prefs = gui.displayPreferencesMenu()
    print(prefs)
    running = prefs[0]
    walking_value = prefs[1]
    biking_value = prefs[2]
    transit_value = prefs[3]
    education_value = prefs[4]
    safety_value = prefs[5]
    addresses = gui.displayAddressesMenu()
    running = addresses[0]
    addresses = addresses[1:]

    if not running:
        break

    print("walking score: {} biking score: {} transit score: {}".format(walking_value, biking_value, transit_value))
    
