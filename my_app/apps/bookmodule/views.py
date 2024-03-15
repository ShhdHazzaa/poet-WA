from django.shortcuts import render

def index(request):
    #study the req
    return render(request, 'bookmodule/index.html')
     
