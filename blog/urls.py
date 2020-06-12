from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # api to post a comment
    path('postcomment', views.postcomment, name='postcomment'),

    path('', views.BlogHome, name='BlogHome'),
    path('<str:slug>', views.BlogPost, name='BlogPost'),

]
