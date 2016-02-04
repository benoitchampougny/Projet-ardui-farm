from django.conf.urls import url

from . import views

urlpatterns = [
    # Home views
    url(r'^$', views.home, name='home'),
    url(r'^network$', views.network, name='network'),
    url(r'^network/open/(?P<component_type>\w+)/(?P<component_id>\d+)$', views.network, name='network-open'),

    # Generic Detail view that will route to the specific one
    url(r'^network/detail/(?P<component_type>\w+)/(?P<component_id>\d+)$',
        views.component_detail,
        name='network-component-detail'),

    # Specific Detail Views
    url(r'^network/detail_arduino/(?P<id>\d+)$', views.detail_arduino, name='network-arduino-detail'),
    url(r'^network/detail_raspberry/(?P<id>\d+)$', views.detail_raspberry, name='network-raspberry-detail'),
    url(r'^network/detail_sensor/(?P<id>\d+)$', views.detail_sensor, name='network-sensor-detail'),
    url(r'^network/detail_actuator/(?P<id>\d+)$', views.detail_actuator, name='network-actuator-detail'),

    # I2C Connection
    url(r'^network/add_i2c_connection/(?P<component_type>\w+)/(?P<id>\d+)$',
        views.add_i2c_connection,
        name='network-add-i2c'),

    # Create Component
    url(r'^network/create_component$', views.create_component, name='network-create-component'),

]
