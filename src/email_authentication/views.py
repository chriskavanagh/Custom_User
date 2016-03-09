from django.shortcuts import render, redirect
from custom_user.admin import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from custom_user.models import UserSession
#from custom_user.forms import CustomUserCreationForm



# Create your views here.
def home(request):
    return render(request, 'home.html', {})
    

def my_login(request):
    return render(request, 'login.html', {})
    
    
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    
    if user is not None and user.is_active:
        login(request, user)       
        return redirect('loggedin')
    else:
        messages.warning(request, 'Please Provide A Valid Username Or Password.')
        return redirect('login')
        
        
def loggedin(request):
    return render(request, 'login.html', {'user': request.user})
    
    
def invalid_login(request):
    return render(request, 'invalid_login.html',{})
    
    
@login_required   
def my_logout(request):
    logout(request)
    return redirect('home')
    
    
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_success')
        
    else:
        form = UserCreationForm()
        
    context = {'form': form}
    
    return render(request, 'register.html', context)


def register_success(request):
    return render(request, 'register_success.html', {})
    
    
# find & del user session(s) by UserSession in models.py    
def delete_user_sessions(user):
    user_sessions = UserSession.objects.filter(user = user)
    for user_session in user_sessions:
        user_session.session.delete()
    