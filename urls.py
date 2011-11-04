from django.conf.urls.defaults import *
from django.conf import settings

from ccradio import views

#static
from django.views.static import serve

#admin
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.base),

    #admin
    url(r'^admin/', include(admin.site.urls)),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^.*?media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
