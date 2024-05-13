from django.views.generic import ListView, DetailView
from .models import Poem, Poet

class PoemListView(ListView):
    model = Poem
    template_name = 'bookmodule/poem_list.html'

class PoemDetailView(DetailView):
    model = Poem
    template_name = 'bookmodule/poem_detail.html'

class PoetListView(ListView):
    model = Poet
    template_name = 'bookmodule/poet_list.html'

class PoetDetailView(DetailView):
    model = Poet
    template_name = 'bookmodule/poet_detail.html'
