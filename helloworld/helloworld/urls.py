from django.conf.urls import * 
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^hello', 'helloworld.views.index'),
]
