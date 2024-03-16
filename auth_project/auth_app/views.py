from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout

# Create your views here.
def register_view(request):
    if(request.method=='post'):
        form=UserCreationForm(request.POST)
        if(form.is_valid()):
            user=form.save()
            login(request,user)

def login_view(request):
    pass

def dashboard_view(request):
    pass

def logout_view(request):
    pass

