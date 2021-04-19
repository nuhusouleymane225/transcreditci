from django.shortcuts import render, redirect
from .forms import PersonalDataForm
from .models import PersonalData, Commentaire, Newsletter
# Create your views here.
from django.contrib import messages

def home(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about-us.html')


def contact(request):
    return render(request, 'pages/contact-us.html')


def vehicule(request):
    return render(request, 'pages/vehicule.html')


def vehicule_detail(request):
    return render(request, 'pages/shop-detail.html')


def formulaire( request):
     form = PersonalDataForm(request.POST or None)
     if form.is_valid():
         obj=PersonalData.objects.create(** form.cleaned_data)
         obj.save()
         form = PersonalDataForm()
         print('data valid')
         messages.success(request, "Votre dossier a été soumis avec succes, vous allez être recontacté!")
     else: 
         print('data is not valid')
         messages.warning(request, "Une erreur s'est produite!")
     context={'form': form}
     template_name = 'pages/formulaire.html'
     return render(request, template_name, context)


def details(request):
    return render(request, 'pages/shop-detail.html')
