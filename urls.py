from django.conf.urls.defaults import *
from django.conf import settings

from ccradio import views
from panel import views  as pviews

#static
from django.views.static import serve

#admin
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.base),
    url(r'^play/', views.play),
    url(r'^panel/', pviews.base),
    url(r'^logout/', pviews.logout_user),
    
    #admin
    url(r'^admin/', include(admin.site.urls)),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^.*?media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
