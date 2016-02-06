from django.conf.urls import url

from . import views

app_name = 'broadcast'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^groupme_home/$', views.GroupMeHomeView.as_view(),name='groupme_home'),
    url(r'^groupme_home/save_group/$', views.saveGroups, name='save_groups'),
    url(r'^groupme_home/add_groupme_api/$', views.addGroupMeApi, name='add_groupme_api'),
    url(r'^groupme_home/wipe_groups/$', views.wipeGroups, name='wipe_groups'),
    url(r'^twitter_home/$', views.TwitterHomeView.as_view(),name='twitter_home'),
    url(r'^twitter_home/add_twitter/$', views.addTwitter, name='add_twitter'),
    url(r'^twitter_home/save_twitter/$', views.saveTwitter, name='save_twitter'),
    url(r'^twitter_home/remove_twitter/$', views.removeTwitter, name='remove_twitter'),
    url(r'^send_message/$', views.sendMessage, name='send_message'),
]