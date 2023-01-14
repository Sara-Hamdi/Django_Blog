from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name="home"),
    path('Boards/<int:board_id>/', views.board_topics, name="board_topics"),
    path('Boards/<int:board_id>/new/',
         views.new_topics, name='new_topic'),

    path('Boards/<int:board_id>/topics/<int:topic_id>/',
         views.topic_posts, name='topic_posts'),
    path('Boards/<int:board_id>/topics/<int:topic_id>/reply/',
         views.reply_topic, name='reply_topic')



]
