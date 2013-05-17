from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^index$', 'demo.views.index_view', name='index_view'),
    url(r'^post/(\d*)$', 'demo.views.post', name='post'),
    url(r'^hora$', 'demo.views.hora_actual', name='hora'),
    url(r'^hora_hot_trick$', 'demo.views.hora_actual_hot_trick', name='hora_hot_trick'),
    url(r'^agregar$', 'demo.views.agregar', name='agregar'),
    # Examples:
    url(r'^$', 'demo.views.home', name='home'),
    # url(r'^app/', include('app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
