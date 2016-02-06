from django.conf.urls import url

from . import views
from . import api

urlpatterns = [
    # Home views
    url(r'^$', views.home, name='home'),
    url(r'^network$', views.network, name='network'),
    url(r'^network/open/(?P<component_type>\w+)/(?P<component_id>\d+)$', views.network, name='network-open'),

    # Generic Detail view that will route to the specific one
    url(r'^network/detail/(?P<component_type>\w+)/(?P<component_id>\d+)$',
        views.component_detail,
        name='network-component-detail'),

    # I2C Connection
    url(r'^network/add_i2c_connection/(?P<component_type>\w+)/(?P<id>\d+)$',
        views.add_i2c_connection,
        name='network-add-i2c'),
    url(r'^network/remove_i2c_connection/(?P<component_type>\w+)/(?P<component_id>\d+)/(?P<dst_component_type>\w+)/(?P<dst_component_id>\d+)$',
        views.remove_i2c_connection,
        name='network-remove-i2c'),

    # Create Component
    url(r'^network/create_component$', views.create_component, name='network-create-component'),

    # APIs
    url(r'^api/get_component_model$',
        api.get_component_model,
        name='api-component-model')

]
