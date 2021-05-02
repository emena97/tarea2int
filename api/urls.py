"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from webapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/<str:id_artist>/albums', views.AlbumPG.as_view()),
    path('artists/<str:id_artist>', views.ArtistID.as_view()),
    path('artists', views.ArtistList.as_view()),
    path('albums', views.AlbumList.as_view()),
    path('albums/<str:id_album>/tracks', views.TrackPG.as_view()),
    path('tracks', views.TrackList.as_view()),
    path('artists/<str:id_artist>/tracks', views.TracksArtist.as_view()),
    path('albums/<str:id_album>', views.AlbumID.as_view()),
    path('tracks/<str:id_track>', views.TrackID.as_view()),
    path('artists/<str:id_artist>/albums/play', views.ArtistPlay.as_view()),
    path('albums/<str:id_album>/tracks/play', views.AlbumPlay.as_view()),
    path('tracks/<str:id_track>/play', views.TrackPlay.as_view()),
]
