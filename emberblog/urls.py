from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='home'),
    url(r'^blogs/$', 'blog.views.index'),
    url(r'^about/$', 'blog.views.index'),
    url(r'^api/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
