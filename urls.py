from django.conf.urls.defaults import *

urlpatterns = patterns('filebrowser.views',
    
    url(r'^(?P<dir_name>[_a-zA-Z0-9./\- ]+)/mkdir/', 'mkdir'),
    url(r'^(?P<dir_name>[_a-zA-Z0-9./\- ]+)/upload/', 'upload'),
    url(r'^(?P<dir_name>[_a-zA-Z0-9./\- ]+)/delete/$', 'delete'),
    url(r'^(?P<dir_name>[_a-zA-Z0-9./\- ]+)/makethumbs/$', 'makethumb'),
    url(r'^(?P<dir_name>[_a-zA-Z0-9./\- ]+)/makethumb/(?P<file_name>[a-zA-Z0-9._\- ]+)', 'makethumb'),
    url(r'^(?P<dir_name>[_a-zA-Z0-9./\- ]+)/generateimages/$', 'generateimages'),
    url(r'^(?P<dir_name>[_a-zA-Z0-9./\- ]+)/generateimages/(?P<file_name>[a-zA-Z0-9._\- ]+)', 'generateimages'),
    url(r'^(?P<dir_name>[_a-zA-Z0-9./\- ]+)/rename/(?P<file_name>[a-zA-Z0-9._\- ]+)', 'rename'),
    url(r'^(?P<dir_name>[_a-zA-Z0-9./\- ]+)/change/(?P<file_name>[a-zA-Z0-9._\- ]+)', 'change'),
    url(r'^mkdir/', 'mkdir'),
    url(r'^upload/', 'upload'),
    url(r'^delete/$', 'delete'),
    url(r'^makethumbs/$', 'makethumb'),
    url(r'^makethumb/(?P<file_name>[a-zA-Z0-9._\- ]+)', 'makethumb'),
    url(r'^generateimages/$', 'generateimages'),
    url(r'^generateimages/(?P<file_name>[a-zA-Z0-9._\- ]+)', 'generateimages'),
    url(r'^rename/(?P<file_name>[a-zA-Z0-9._\- ]+)', 'rename'),
    url(r'^change/(?P<file_name>[a-zA-Z0-9._\- ]+)', 'change'),
    url(r'^(?P<dir_name>[_a-zA-Z0-9./\- ]+)/$', 'index'),
    url(r'^$', 'index', name='filebrowser-index'),

)
