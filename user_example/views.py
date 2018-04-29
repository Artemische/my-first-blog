from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import InformForm
from random import randint
from .models import Inform


def index(request):
    informs = Inform.objects.order_by('-group', 'surname')
    return render(request, 'user_example/index.html', {'informs':informs})

def rob(request):
    informs = Inform.objects.filter(group='10706117').order_by('surname')
    return render(request, 'user_example/06.html', {'informs':informs})

def avt(request):
    informs = Inform.objects.filter(group='10703117').order_by('surname')
    return render(request, 'user_example/03.html', {'informs':informs})

def avtt(request):
    informs = Inform.objects.filter(group='10703217').order_by('surname')
    return render(request, 'user_example/04.html', {'informs':informs})


def landing(request):
    name = 'ConfigArtem'
    current_day = '26.04.2018'
    tasks = randint(1,4)
    form = InformForm(request.POST or None,initial={'task': tasks})
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
      #  print(data["name"])

        new_form = form.save()
        return redirect('index')
    return render(request, 'user_example/landing.html', locals())




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)
