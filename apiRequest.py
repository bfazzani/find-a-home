import requests

apiKEY = "b5093bcc1c8c8c8a5f263745f82a5d39"
baseURL = "http://api.walkscore.com/score"

r = requests.get("""http://api.walkscore.com/score?format=json&
address=1119%8th%20Avenue%20Seattle%20WA%2098101&lat=47.6085&
lon=-122.3295&transit=1&bike=1&wsapikey=<YOUR-WSAPIKEY>""")

x = r.json()

print(x)
print(x["status"])
print(x["walkscore"])
print(x["transit"])
print(x["bike"])
print(x)
