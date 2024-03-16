from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if(request.method=='post'):
        form=UserCreationForm(request.POST)
        if(form.is_valid()):
            user=form.save()
            login(request,user)

def login(request):
    pass

def dashboard(request):
    pass

def logout(request):
    pass

