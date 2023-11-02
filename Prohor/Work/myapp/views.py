from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Staff
from .forms import StaffForm

def index(request):
    tasks = Staff.objects.order_by('-id')
    return render(request, 'myapp/index.html',{
    'title': 'Главная страница сайта', 'tasks': tasks})

def RSP(request):
    return render(request, 'myapp/RSP.html')

def create(request):
    error = ''
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = StaffForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'myapp/create.html', context)


