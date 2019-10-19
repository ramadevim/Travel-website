from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from .models import Register
from .forms import RegForm,LoginForm,ContactForm
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
        
            return redirect('/')

    else:
        form=ContactForm()
    return render(request,'contact.html',{'form':form})


def Register(request):
    if request.method == 'POST':
        form=RegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Accounted created successfully','success')
            return redirect('/')

    else:
        form=RegForm()
    return render(request,'reg.html',{'form':form})

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Register')
        else:
            print("error.......")

    return render(request, "login.html", context=context)



def logout_page(request):
    logout(request)
    return redirect('/')