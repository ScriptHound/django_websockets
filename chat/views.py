from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def room(request, room_name):
    context = {
        'room_name': room_name
    }
    return render(request, 'room.html', context)


class ChatView(TemplateView):

    def get(self, request):
        return render(request, 'index.html')


