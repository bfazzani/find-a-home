import googleMaps as maps
import gui
import walkScore as ws

address = "1600 Amphitheatre Parkway, Mountain View, CA 94043, USA"
adData = maps.getCoordFromAddress(address)
transitScores = ws.getTransitScores(address, adData[0], adData[1])
print("{ad} at lat:{lat} lng:{lng}".format(ad=address, lat=adData[0], lng=adData[1]))
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
    
