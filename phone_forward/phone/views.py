from django.shortcuts import render, redirect
from phone import models
from django.views import View

class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, "index.html")
    
    def post(self, request):
        func = models.Func.createFunc(phone_number=request.POST['phone_number'], alias=request.POST['alias'])
        context = {}
        if(func is not None):
            func.save()
        else:
            context = {
                'error': 'funcionario não criado, tente novamente :('
            }
        return redirect('registered_func')


class EditFunc(View):
    template_name = 'edit_func.html'

    def get(self, request, phone_number):
        func = models.Func.objects.get(phone_number = phone_number)
        return render(request, "edit_func.html", {
            'func': func
    })

    def post(self, request, phone_number):
        func = models.Func.objects.get(phone_number = phone_number)
        func.phone_number = request.POST['phone_number']
        func.alias = request.POST['alias']
        func.save()
        return redirect('registered_func')


def registered_func(request):
    all_func = models.Func.objects.all()
    context = {
        "all_func":all_func
    }
    return render(request, "registered_func.html", context)


def remove_func(request, phone_number):
    func = models.Func.objects.get(phone_number = phone_number)
    func.delete()
    return redirect('registered_func')