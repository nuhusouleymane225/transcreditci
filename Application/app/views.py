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


def formulaire( request):
     form = PersonalDataForm(request.POST or None)
     if form.is_valid():
         obj=PersonalData.objects.create(** form.cleaned_data)
         obj.save()
         form = PersonalDataForm()
         print('data valid')
     else: 
         print('data is not valid')
     context={'form': form}
     template_name = 'pages/formulaire.html'
     return render(request, template_name, context)


def details(request):
    return render(request, 'pages/shop-detail.html')


#### Tous ce qui est en bas est à supprimer une fois qu'on a creer les slug pour prendre
### les id en parametres j'ai fais cala chap chap pour qu'on presente a Amissob tu comprends un peu non Amissob rire ... 

def detail_renault_kwid(request):
    return render(request, 'pages/vehicules/detail_renault_kwid.html')

def detail_renault_logan(request):
    return render(request, 'pages/vehicules/detail_renault_logan.html')

def detail_suzuki_alto(request):
    return render(request, 'pages/vehicules/detail_suzuki_alto.html')

def detail_suzuki_dzire(request):
    return render(request, 'pages/vehicules/detail_suzuki_dzire.html')

def detail_suzuki_presso(request):
    return render(request, 'pages/vehicules/detail_suzuki_presso.html')

def detail_suzuki_swift(request):
    return render(request, 'pages/vehicules/detail_suzuki_swift.html')

def detail_toyota_corolla(request):
    return render(request, 'pages/vehicules/detail_toyota_corolla.html')

def detail_toyota_starlet(request):
    return render(request, 'pages/vehicules/detail_toyota_starlet.html')

