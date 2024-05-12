from django.shortcuts import render
from .models import Poem, Poet

def home(request):
    return render(request, 'base.html')

def poem_detail(request, pk):
    poem = Poem.objects.get(pk=pk)
    return render(request, 'bookmodule/poem_detail.html', {'poem': poem})

def poet_detail(request, pk):
    poet = Poet.objects.get(pk=pk)
    return render(request, 'bookmodule/poet_detail.html', {'poet': poet})

def poet_list(request):
    poets = Poet.objects.all()
    return render(request, 'bookmodule/poet_list.html', {'poets': poets})
def poem_list(request):
    poems = Poem.objects.all()
    return render(request, 'bookmodule/poem_list.html', {'poems': poems})
