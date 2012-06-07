from django.conf.urls.defaults import *
from django.conf import settings

from ccradio import views

#static
from django.views.static import serve

#admin
from django.contrib import admin
import registration
admin.autodiscover()


urlpatterns = patterns('',
    (r'^$', 'views.base'),
    (r'^play/', 'views.play'),
    (r'^about/', 'views.about'),
    (r'^panel/', 'ccradio.panel.views.base'),
    (r'^thanks/', 'views.thanks'),
    (r'^tos/', 'views.tos'),
    (r'^logout/', 'ccradio.panel.views.logout_user'),
    
    #admin
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^.*?media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
