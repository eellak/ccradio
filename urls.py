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
    (r'^$', 'ccradio.views.base'),
    (r'^play/', 'ccradio.views.play'),
    (r'^about/', 'ccradio.views.about'),
    (r'^panel/edit/', 'ccradio.panel.views.edit'),
    (r'^panel/', 'ccradio.panel.views.base'),
    (r'^thanks/', 'ccradio.views.thanks'),
    (r'^tos/', 'ccradio.views.tos'),
    (r'^logout/', 'ccradio.panel.views.logout_user'),

    #admin
    (r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset'),
    (r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^admin/reset/(?P<uidb35>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^admin/reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^.*?media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
