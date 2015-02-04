from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'pcbuilder.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^behuizingen/', 'pcbuilder.views.behuizingen'),
    url(r'^processoren/', 'pcbuilder.views.processoren'),
    url(r'^geheugen/', 'pcbuilder.views.geheugen'),
    url(r'^gpu/', 'pcbuilder.views.grafische'),
    url(r'^hardeschijven/', 'pcbuilder.views.harde'),
    url(r'^koelingen/', 'pcbuilder.views.koeling'),
    url(r'^moederborden/', 'pcbuilder.views.moederborden'),
    url(r'^optischeschijven/', 'pcbuilder.views.dvd'),
    url(r'^voedingen/', 'pcbuilder.views.voeding'),
    url(r'^detail/', 'pcbuilder.views.detail'),
    url(r'^select/', 'pcbuilder.views.select'),
    url(r'^viewd/', 'pcbuilder.views.Viewers'),
    url(r'^deselect/', 'pcbuilder.views.deselect'),
    url(r'^contact/', 'pcbuilder.views.contact'),
    url(r'^mail/', 'pcbuilder.views.mail'),
    url(r'^dashboard/', 'pcbuilder.views.dashboard'),
    url(r'^login/', 'pcbuilder.views.login'),
    url(r'^registreer/', 'pcbuilder.views.registreer'),
    url(r'^loguit/', 'pcbuilder.views.loguit'),
    url(r'^bestellingen/', 'pcbuilder.views.bestellingen'),
    url(r'^wijzigRechten/', 'pcbuilder.views.wijzigRechten'),
    url(r'^bestel/', 'pcbuilder.views.bestel'),


    url(r'^search/', 'pcbuilder.views.search'),

    url(r'^user/(?P<product>\w{0,50})/$', 'pcbuilder.views.pages'),
    url(r'^user/(?P<aantal>\w{0,50})/$', 'pcbuilder.views.pages'),
    url(r'^user/(?P<pagina>\w{0,50})/$', 'pcbuilder.views.pages'),
    url(r'^user', 'pcbuilder.templatetags.keyvalue'),

    url(r'^contact$', 'pcbuilder.views.contact'),
    url(r'^contact/$', 'pcbuilder.views.contact', name='contact'),
    url(r'^compile/', 'pcbuilder.views.compile', name="compile"),
)