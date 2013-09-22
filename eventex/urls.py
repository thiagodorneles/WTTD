from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('eventex.core.urls', namespace='core')),

    # url(r'^$', 'eventex.core.views.homepage', name='homepage'),
    # url(r'^inscricao/$', 'eventex.subscriptions.views.subscribe', name='subscribe'),
    # url(r'^inscricao/(\d)+/$', 'eventex.subscriptions.views.detail', name='detail')
    
    # url(r'^eventex/', include('eventex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
