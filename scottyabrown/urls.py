from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from athensrock import views as arock_views
from home import views as home_views

urlpatterns = [
    url(r'^$', home_views.index, name='home'),
    url(r'^athensrock/index', arock_views.index, name='arock_index'),
    url(r'^callback/$', arock_views.callback, name='callback'),
    url(r'^add_songs/', arock_views.add_songs, name='arock_add_songs'),
    url(r'^athensrock/dashboard/', arock_views.dashboard, name='arock_dashboard'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
