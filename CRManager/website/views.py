from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    # Login Check
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # User Authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Signed In!')
            return redirect('home')
        else:
            messages.success(request, 'Failed to Log in. Please Try again!')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You have signed out. See you later!')
    return redirect('home')

def register_user(request):
    # If the user fills out the form completely, it will process registration and login for the new user.
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authentication and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registered Successfully! Congratulations!')
            return redirect('home')
    # If the form is not filled completely, it just redirects the user to the register page again.
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})