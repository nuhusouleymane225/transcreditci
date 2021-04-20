from . import views
from django.conf.urls import url


urlpatterns = [
  
    url(r'^$', views.home, name='index',),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^vehicule/$', views.vehicule, name='vehicule'),
    url(r'^details/$', views.details, name='details'),
    url(r'^formulaire/$', views.formulaire, name='formulaire'),


    ### A Supprimer aussi apres

    url(r'^detail_renault_kwid/$', views.detail_renault_kwid, name='detail_renault_kwid'),
    url(r'^detail_renault_logan/$', views.detail_renault_logan, name='detail_renault_logan'),
    url(r'^detail_suzuki_alto/$', views.detail_suzuki_alto, name='detail_suzuki_alto'),
    url(r'^detail_suzuki_dzire/$', views.detail_suzuki_dzire, name='detail_suzuki_dzire'),
    url(r'^detail_suzuki_presso/$', views.detail_suzuki_presso, name='detail_suzuki_presso'),
    url(r'^detail_suzuki_swift/$', views.detail_suzuki_swift, name='detail_suzuki_swift'),
    url(r'^detail_toyota_corolla/$', views.detail_toyota_corolla, name='detail_toyota_corolla'),
    url(r'^detail_toyota_starlet/$', views.detail_toyota_starlet, name='detail_toyota_starlet'),



]