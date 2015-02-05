from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'pcbuilder.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^behuizingen/', 'pcbuilder.views.renderToTemplate'),
    url(r'^processoren/', 'pcbuilder.views.renderToTemplate'),
    url(r'^geheugen/', 'pcbuilder.views.renderToTemplate'),
    url(r'^grafische/', 'pcbuilder.views.renderToTemplate'),
    url(r'^harde/', 'pcbuilder.views.renderToTemplate'),
    url(r'^koeling/', 'pcbuilder.views.renderToTemplate'),
    url(r'^moederborden/', 'pcbuilder.views.renderToTemplate'),
    url(r'^dvd/', 'pcbuilder.views.renderToTemplate'),
    url(r'^voeding/', 'pcbuilder.views.renderToTemplate'),
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
    url(r'^wijzigRechten/', 'pcbuilder.views.wijzigRechten'),


    url(r'^search/', 'pcbuilder.views.search'),

    url(r'^user/(?P<product>\w{0,50})/$', 'pcbuilder.views.pages'),
    url(r'^user/(?P<aantal>\w{0,50})/$', 'pcbuilder.views.pages'),
    url(r'^user/(?P<pagina>\w{0,50})/$', 'pcbuilder.views.pages'),
    url(r'^user', 'pcbuilder.templatetags.keyvalue'),

    url(r'^contact$', 'pcbuilder.views.contact'),
    url(r'^contact/$', 'pcbuilder.views.contact', name='contact'),
    url(r'^compile/', 'pcbuilder.views.compile', name="compile"),
)