from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.game_list),
    url(r'^game/(?P<pk>[0-9]+)/$', views.game_play),
    url(r'^game/new/$', views.game_new, name='game_new'),
    url(r'^game/(?P<pk>[0-9]+)/edit/$', views.game_edit, name='game_edit'),
    url(r'^game/(?P<pk>[0-9]+)/delete/$', views.game_delete),
]