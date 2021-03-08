from django.urls import path

from chat.views import ChatView, room

urlpatterns = [
    path('', ChatView.as_view(), name='index'),
    path('<str:room_name>/', room, name='room'),
]
