from django.shortcuts import render
from django.contrib import messages

from .forms import MemberForm


def homepage(request):
    if request.method == 'POST':
        # initialise le formulaire avec les données envoyés
        form = MemberForm(request.POST)

        # si les données sont valides
        if form.is_valid and not form.errors:
            form.save()  # enregistrer le membre en base de données
            form = MemberForm()  # créer un nouveau formulaire vide

            # enregistrer un message de succès
            messages.success(request, 'Merci pour ton inscription!')
    else:
        form = MemberForm()  # le formulaire à afficher sur la page

    return render(request, 'members/index.html', locals())


def member_view(request, member_id):
    return render(request, 'members/member_view.html', locals())
