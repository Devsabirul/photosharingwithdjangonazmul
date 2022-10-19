from django.shortcuts import redirect, render
from login.forms import HandelLoginForm
from django.contrib.auth import authenticate, login as auth_login, logout
# Create your views here.


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = HandelLoginForm(request.POST, data=request.POST)
            if fm.is_valid():
                user_name = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=user_name, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('/dashboard')
        else:
            fm = HandelLoginForm()
        return render(request, 'login/login.html', {'form': fm})
    else:
        return redirect("/dashboard")

# logout


def user_logout(request):
    logout(request)
    return redirect('/')
