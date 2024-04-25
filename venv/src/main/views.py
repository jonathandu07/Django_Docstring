#  Module pour les templates de l'app main
# Ici je met les composants récurants et les pages indispensables

from django.http import HttpResponse

# Je créais une fonction pour afficher ma page
# cette fonction s'appelle index et renvoie vers la page principal (page d'accueil)
# Je donne le paramètre 'request' pour qu'il aille faire une requète http
def index(request):
    # Dans cette fonction je retourne un objet qui s'appelle httpResponse
    return HttpResponse("<h1>Hola Jonathan !</h1>")