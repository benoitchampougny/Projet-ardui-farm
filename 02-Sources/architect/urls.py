"""
  Copyright (c) 2016 Benoit CHAMPOUGNY.  All right reserved.

  This file is part of Arduifarm

  Arduifarm is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  Arduifarm is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
      along with Arduifarm.  If not, see <http://www.gnu.org/licenses/>. 2
"""

from django.conf.urls import url

from . import views
from . import api

urlpatterns = [
    # Home views
    url(r'^$', views.home, name='home'),
    url(r'^network$', views.network, name='network'),
    url(r'^network/open/(?P<component_id>\d+)$', views.network, name='network-open'),
    url(r'^location$', views.location, name='location'),
    url(r'^location/open/(?P<component_type>\w+)/(?P<component_id>\d+)$', views.location, name='location-open'),

    # Generic Detail view that will route to the specific one
    url(r'^network/detail/(?P<component_id>\d+)$',
        views.component_detail,
        name='network-component-detail'),
    url(r'^location/detail/(?P<component_type>\w+)/(?P<component_id>\d+)$',
        views.location_component_detail,
        name='location-component-detail'),
    url(r'^location/remove_location_connection/(?P<component_type>\w+)/(?P<component_id>\d+)/(?P<dst_component_type>\w+)/(?P<dst_component_id>\d+)$',
        views.remove_location_connection,
        name='location-remove-location'),

    # Location Connection
    url(r'^location/add_location_connection/(?P<component_type>\w+)/(?P<selectTable>\w+)/(?P<id>\d+)$',
        views.add_location_connection,
        name='location-add-location'),

    # I2C Connection
    url(r'^network/add_i2c_connection/(?P<id>\d+)$',
        views.add_i2c_connection,
        name='network-add-i2c'),
    url(r'^network/remove_i2c_connection/(?P<component_id>\d+)/(?P<dst_component_id>\d+)$',
        views.remove_i2c_connection,
        name='network-remove-i2c'),

    # I2C Connection
    url(r'^network/add_dio_connection/(?P<id>\d+)$',
        views.add_dio_connection,
        name='network-add-dio'),
    url(r'^network/remove_dio_connection/(?P<component_id>\d+)/(?P<dst_component_id>\d+)$',
        views.remove_dio_connection,
        name='network-remove-dio'),

    # Sketch generation
    url(r'^network/generate_sketch/(?P<arduino_id>\d+)$',
        views.generate_sketch,
        name='network-generate_sketch'),


    # Create Component
    url(r'^network/create_component$', views.create_component, name='network-create-component'),

    # Create location Component
    url(r'^location/create_component$', views.create_location_component, name='location-create-component'),

    # APIs
    url(r'^api/get_component_model$',
        api.get_component_model,
        name='api-component-model')

]
