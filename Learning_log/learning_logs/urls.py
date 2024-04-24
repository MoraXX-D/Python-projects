"""Define URL pattern for learning_logs"""

from django.urls import path,include

from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # show all topics
    path('topics/', views.topics, name='topics'),
    # detail page for single topic
    path('topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic,name='new_topic'),


]