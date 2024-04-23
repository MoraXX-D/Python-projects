"""Define URL pattern for learning_logs"""

from django.urls import path,include

from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # show all topics
    path('topics/', views.topics, name='topics'),
]