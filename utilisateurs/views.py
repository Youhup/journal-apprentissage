from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """inscrire un nouvel utilisateur"""
    if request.method != "POST":
        #Afficher un formulaire d'inscrioption vide
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #ouvrir la session de l'utilisateur et le rediriger vers la page d'acceil
            login(request, new_user)
            return redirect("journaux_apprentissage:index")
    #Afficher un formulaire vierge ou invalide
    context = {'form': form}
    return render(request,'registration/register.html', context)


