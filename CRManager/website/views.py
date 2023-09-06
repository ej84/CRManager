from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all()
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
        return render(request, 'home.html', {'records':records})

def login_user(request):
    # Can be used to create separate login page, form, or anything like that.
    pass

def logout_user(request):
    # Log out and redirects to the home page.
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

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up Records
        customer_record = Record.objects.get(id=pk) # use .get() to get single object.
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view that page!")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, 'Record deleted.')
        return redirect('home')
    else:
        messages.success(request, 'You are not allowed to perform this action. Please sign in first!')
        return redirect('home')
    
def new_record(request):
    return render(request, 'new_record.html', {})