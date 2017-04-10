"""apk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth.decorators import login_required

from apkapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^musicshow/$', views.MusicTrackDetails.as_view(), name='music_show'),
    url(r'^get_title_data/$', views.get_title_data, name='get_title_data'),
    url(r'^addmusic/$', views.Add_Music_Details.as_view(), name='addmusic'),
    url(r'^editmusic/(?P<id>\d+)/$', views.EditMusicTrackDetails.as_view() , name='editmusic'),
    # url(r'^music_show/$', login_required(views.show_MusicTrack_Details(), login_url="/") , name='music_show'),
    url(r'^genresshow/$', views.GenresDetails.as_view(), name='genres_show'),
    url(r'^addgenres/$', views.Add_Genres_Details.as_view(), name='addgenres'),
    url(r'^editgenres/(?P<id>\d+)/$', views.EditGenresDetails.as_view(), name='editgenres'),

]

