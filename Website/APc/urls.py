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
    url(r'^detail/', 'pcbuilder.views.detail'),
    url(r'^select/', 'pcbuilder.views.select'),
    url(r'^viewd/', 'pcbuilder.views.Viewers'),
    url(r'^deselect/', 'pcbuilder.views.deselect'),
    url(r'^contact/', 'pcbuilder.views.contact'),
    url(r'^mail/', 'pcbuilder.views.mail'),

    #geen idee wat dit allemaal is
    url(r'^user/(?P<product>\w{0,50})/$', 'pcbuilder.views.pages'),
    url(r'^user/(?P<aantal>\w{0,50})/$', 'pcbuilder.views.pages'),
    url(r'^user/(?P<pagina>\w{0,50})/$', 'pcbuilder.views.pages'),
    url(r'^user', 'pcbuilder.templatetags.keyvalue'),

    url(r'^contact$', 'pcbuilder.views.contact'),
    url(r'^contact/$', 'pcbuilder.views.contact', name='contact'),
)