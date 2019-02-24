import requests
import urllib.parse as url

apiKey = "AIzaSyCox6ItoDysfyjbB5YPhPBE2-S2RYtTcGQ"
baseURL = "https://maps.googleapis.com/maps/api/geocode/json?"

def getCoordFromAddress(address):
    requestString = baseURL + url.urlencode({"address":address, "key":apiKey})
    r = requests.get(requestString)
    x = r.json()
    lat = x["results"][0]["geometry"]["location"]["lat"]
    lng = x["results"][0]["geometry"]["location"]["lng"]
    return (lat, lng)
