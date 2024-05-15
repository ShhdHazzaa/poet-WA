from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Poem, Poet
from .forms import PoemForm, PoetForm
class PoemListView(ListView):
    model = Poem
    template_name = 'bookmodule/poem_list.html'

class PoemDetailView(DetailView):
    model = Poem
    template_name = 'bookmodule/poem_detail.html'

class PoemCreateView(CreateView):
    model = Poem
    form_class = PoemForm
    template_name = 'bookmodule/poem_form.html'

class PoemUpdateView(UpdateView):
    model = Poem
    form_class = PoemForm
    template_name = 'bookmodule/poem_form.html'

class PoemDeleteView(DeleteView):
    model = Poem
    success_url = reverse_lazy('poem_list')
    template_name = 'bookmodule/poem_confirm_delete.html'

class PoetListView(ListView):
    model = Poet
    template_name = 'bookmodule/poet_list.html'

class PoetDetailView(DetailView):
    model = Poet
    template_name = 'bookmodule/poet_detail.html'

class PoetCreateView(CreateView):
    model = Poet
    form_class = PoetForm
    template_name = 'bookmodule/poet_form.html'

class PoetUpdateView(UpdateView):
    model = Poet
    form_class = PoetForm
    template_name = 'bookmodule/poet_form.html'

class PoetDeleteView(DeleteView):
    model = Poet
    template_name = 'لbookmodule/poet_confirm_delete.html'
    success_url = reverse_lazy('poet_list') 
