# Django_Docstring
 https://www.youtube.com/watch?v=Bn0k9DDYBZM&ab_channel=Docstring


## Commandes Django

1. `python -m venv venv`
- `venv` est le nom donné à notre environnement virtuelle

2. `.\venv\Scripts\Activate.ps1`  ou `venv\Scripts\activate`
- pour activer l'environment virtuel

3. `cd venv`
- Pour aller dans le répertoire `venv`

4. `pip install django`
- Pour installer Django dans l'environment virtuel.

5. `python.exe -m pip install --upgrade pip`
- Pour mettre à jour Django.

### Création du fichier `requierements.txt`

**à l'intérieur de l'environment virtuel**
`pip freeze > requierements.txt`
- Permet de sauvegarder toute les bibliothèques installées dans notre environnement virtuel.

**Pour réinstaller les bibliothèques en se basant sur ce qu'il y a dans le fichier requierements.txt**
``pip install -r requierements.txt`

---


### Création de notre projet
- `django-admin.py startproject main`

### Démarer le serveur
- `python manage.py runserver `