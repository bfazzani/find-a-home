import requests

apiKey = "b5093bcc1c8c8c8a5f263745f82a5d39"
baseURL = "http://api.walkscore.com/score?format=json"

address = "1119%8th%20Avenue%20Seattle%20WA%2098101"
latitude = 47.6085
longitude = -122.3295

requestString = baseURL
requestString += "&address=" + address
requestString += "&lat=" + str(latitude)
requestString += "&lon=" + str(longitude)
requestString += "&transit=1&bike=1"
requestString += "&wsapikey=" + str(apiKey)

print(requestString)

r = requests.get(requestString)

print(r.status_code)
#print(r.text)
x = r.json()

print(x)
#print(x["status"])
#print(x["walkscore"])
#print(x["transit"])
#print(x["bike"])
#print(x)
