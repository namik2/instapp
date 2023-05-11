from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from stats.forms import InstagramAddForm
from stats.models import IntagramStats

# Create your views here.

def user(request):
    instagram_data = IntagramStats.objects.all()
    return render(request,'user.html',{'instagram_data':instagram_data})

class AddInstagramView(CreateView):
    template_name = 'addinstagram.html'
    form_class = InstagramAddForm
    success_url = reverse_lazy('add_instagram')