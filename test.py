# import datetime
#
# n=datetime.datetime.now()
# print(n.year)

import requests

parameters = {
    "name":"Naru"
}

response = requests.get("https://api.agify.io", params=parameters)
print(response.json())
print(response.json()["name"])
print(response.json()["age"])
