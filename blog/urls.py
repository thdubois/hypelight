from django.conf.urls import url, patterns

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
url(r'^$', views.index, name='index'),
url(r'^articles/$', views.articles, name='articles'),
url(r'^index/$', views.index, name='index'),
url(r'^galerie/$', views.galerie, name='galerie')]


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)