from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect,resolve_url
from django.contrib.auth.decorators import login_required
from users.forms import SignUpForm,LoginForm
#Static Views


@login_required(login_url='users/login')
def profileView(request):
    return render(request,"ui/profile.html")

def logoutView(request):
    logout(request)
    return render(request,"ui/index.html")


def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'ui/signup.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'ui/signin.html', {'form': form})
    