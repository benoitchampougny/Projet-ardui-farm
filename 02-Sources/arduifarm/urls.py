from django.conf.urls import include, url
from django.contrib import admin
import architect

urlpatterns = [
    # Examples:
    # url(r'^$', 'arduifarm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include("architect.urls")),
]
