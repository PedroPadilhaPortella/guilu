from django.shortcuts import render
from libraryApp import models

# Create your views here.
def register(request):
    if(request.method == 'POST'):
        lib = models.Lib(title = request.POST['title'], author = request.POST['author'])
        context = {}
        if(lib is not None):
            lib.save()
        else:
            context = { 'error': 'Livro não cadastrado' }
        return render(request, 'register.html', context)
    return render(request, 'register.html')


def index(request):
    books = models.Lib.objects.all()
    context = {
        "Books": books
    }
    return render(request, 'index.html', context)