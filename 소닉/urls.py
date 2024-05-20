from django.urls import path

from 소닉 import views

app_name = '소닉'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
]