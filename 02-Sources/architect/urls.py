from django.conf.urls import url

from . import views

urlpatterns = [
    # Home views
    url(r'^$', views.home, name='home'),
    url(r'^network$', views.network, name='network'),
]
