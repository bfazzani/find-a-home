import requests
import urllib.parse as url

apiKey = "b5093bcc1c8c8c8a5f263745f82a5d39"
baseURL = "http://api.walkscore.com/score?format=json&"

def getTransitScores(address, lat, lng):
    requestString = baseURL + url.urlencode({"address":address, "lat":lat,
                                             "lon":lng, "transit":1, "bike":1,
                                             "wsapikey":apiKey})
    r = requests.get(requestString)
    x = r.json()
    walk = x["walkscore"]
    bike = x["bike"]
    transit = x["transit"]
    return (walk, bike, transit)
