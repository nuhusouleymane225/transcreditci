from . import views
from django.conf.urls import url


urlpatterns = [
  
    url(r'^$', views.home, name='index',),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^vehicule/$', views.vehicule, name='vehicule'),
    url(r'^details/$', views.details, name='details'),
    url(r'^formulaire/$', views.formulaire, name='formulaire')
]