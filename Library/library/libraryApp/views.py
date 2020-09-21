from django.views import View
from django.shortcuts import redirect, render
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
        "books": books
    }
    return render(request, 'index.html', context)


class EditLib(View):
    template_name = 'edit_lib.html'

    def get(self, request, id):
        book = models.Lib.objects.get(id = id)
        return render(request, "edit_lib.html", {
            'book': book
        })

    def post(self, request, id):
        book = models.Lib.objects.get(id = id)
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
        return redirect('index')


def remove_lib(request, id):
    book = models.Lib.objects.get(id = id)
    book.delete()
    return redirect('index')