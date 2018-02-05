from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from athensrock import views as arock_views
from home import views as home_views
from appalachian_trail import views as at_views

urlpatterns = [
    url(r'^$', home_views.index, name='home'),
    url(r'^athensrock/index', arock_views.index, name='arock_index'),
    url(r'^callback/$', arock_views.callback, name='callback'),
    url(r'^add_songs/', arock_views.add_songs, name='arock_add_songs'),
    url(r'^athensrock/dashboard/', arock_views.dashboard, name='arock_dashboard'),
    url(r'^appalachian_trail/show', at_views.show, name='at_show'),
    url(r'^appalachian_trail/index', at_views.index, name='at_index'),
    url(r'^appalachian_trail/dashboard', at_views.dashboard, name='at_dashboard'),
    url(r'^appalachian_trail/pictures', at_views.pictures, name='at_pictures'),
    url(r'^appalachian_trail/faq', at_views.faq, name='at_faq'),
    url(r'^appalachian_trail/gear', at_views.gear, name='at_gear'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
