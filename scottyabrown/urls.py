from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from athensrock import views as arock_views
from home import views as home_views

urlpatterns = [
    url(r'^$', home_views.index, name='home'),
    url(r'^athensrock/', arock_views.index, name='arock_index'),
    url(r'^song/(?P<id>\d+)/', arock_views.song_detail, name='arock_song_detail'),
    url(r'^callback/$', home_views.callback, name='callback'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
