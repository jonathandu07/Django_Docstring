# Django_Docstring
 https://www.youtube.com/watch?v=Bn0k9DDYBZM&ab_channel=Docstring


## Commandes Django

1. `python -m venv venv`
- `venv` est le nom donné à notre environnement virtuelle

2. `.\venv\Scripts\Activate.ps1`  ou `venv\Scripts\activate` ou `.\Scripts\Activate`
- pour activer l'environment virtuel
- Pour désactiver : `deactivate`


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

**pour y avoir accès sur le réseau local**
- `python manage.py runserver 0.0.0.0:8000`
puis se rendre à l'addresse suivante : http://192.168.10.219:8000

Ne pas oublier de mettre à jour cette ligne : 
```python
ALLOWED_HOSTS = ['192.168.10.219']
```

### Commande pour faire les migration sur la base de données
`python manage.py migrate`

Pour retirer l'erreur lorsqu'on lance le serveur

### Ajouter des templates
**pour faire reconnaitre son fichier template**
1. Aller dans settings.py
2. Aller dans TEMPLATES
3. Ajouter dans `'DIRS : []` le chemin de son dossier templates

**liste de filtres dans Django template**
https://docs.djangoproject.com/en/5.0/ref/templates/builtins/


### Créer une application
`python manage.py startapp nomAPP`
