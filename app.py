import requests

url = "https://v2.jokeapi.dev/joke/Any?type=single"
reponse = requests.get(url)

if reponse.status_code == 200:
    data = reponse.json()
    print("joke : ")
    print(data["joke"])
else:
    print("Error !")