# ue19-lab-05-
Labo5_gestion

Cette application dévelopée en python interroge l'API de JOKESAPI afin de génerer une blague en angalais.


- app.py : Le script qui execute l'API
- Dockerfile : Le fichier qui permet de créer l'image du conteneur
- requirements.txt : La liste des dépendances nécessaires
)

Pour éxecuter via Docker

1. Construire l'image :
   docker build -t ue19-lab-05 .

2. Lancer le conteneur :
   docker run --rm ue19-lab-05
   

Pour éxecuter sans docker

1. Installer les dépendances :
   pip install -r requirements.txt

2. Lancer le script :
   python app.py

## Auteur
Chahid Yakhlifi
