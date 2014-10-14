from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'pcbuilder.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^behuizingen/', 'pcbuilder.views.behuizingen'),
    url(r'^processoren/', 'pcbuilder.views.processoren'),
    url(r'^geheugen/', 'pcbuilder.views.geheugen'),
    url(r'^gpu/', 'pcbuilder.views.gpu'),
    url(r'^hardeschijven/', 'pcbuilder.views.hardeschijf'),
    url(r'^koelingen/', 'pcbuilder.views.koeling'),
    url(r'^moederborden/', 'pcbuilder.views.moederborden'),
    url(r'^optischeschijven/', 'pcbuilder.views.optischeschijf'),
    url(r'^voedingen/', 'pcbuilder.views.voedingen'),
)
