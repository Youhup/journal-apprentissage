from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .forms import TopicForm, EntryForm
from .models import Topic, Entry
def index(request):
    """la page d'accueil pour journal apprentissage"""
    return render(request,'journaux_apprentissage/index.html')
@login_required
def topics(request):
    """Aficher tous les topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'journaux_apprentissage/topics.html',context)
@login_required
def topic(request, topic_id):
    """"Afficher un seul sujet et toutes les entres associes"""
    topic = get_object_or_404(Topic, id=topic_id)
    # Verefier que le sujet appartient au utilisateur courant
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request,'journaux_apprentissage/topic.html',context)
@login_required
def new_topic(request):
    """Ajouter un nouveau sujer"""
    if request.method != "POST":
        #Aucune donnee soumise creer un nouveau sujet
        form = TopicForm()
    else:
        #Donnees POST soumises ,les travailler
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('journaux_apprentissage:topics')
        #Afficher un formulaire vierge ou invalide
    context = {'form':form}
    return render(request,'journaux_apprentissage/new_topic.html',context)
@login_required
def new_entry(request, topic_id):
    """Ajouter un nouvelle entree"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":
        #aucune entree soumise creer un formulaire vierge
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('journaux_apprentissage:topic', topic_id=topic_id)
    #Afficher le formulaire vierge ou invalide
    context = {'topic':topic, 'form':form}
    return render(request,'journaux_apprentissage/new_entry.html',context)
@login_required
def edit_entry(request, entry_id):
    """modifier une entree existante"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != "POST":
        #Requete initiale , remplir le foumulaire avec l'entree actuelle
        form = EntryForm(instance=entry)
    else:
        #donnees post soumises les traiter
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('journaux_apprentissage:topic', topic_id=topic.id)

    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request,'journaux_apprentissage/edit_entry.html',context)