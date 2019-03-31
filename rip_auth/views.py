from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import login, authenticate, logout

from .models import RipUser
from .forms import RipUserCreationForm, RipUserLoginForm
# Create your views here.

@csrf_protect
def register_user(request):
    if request.method == 'POST':
        form = RipUserCreationForm(request.POST)
        print(form.error_messages)
        if form.is_valid():
            form.save()

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])

            login(request, new_user)
            return HttpResponseRedirect('/')
        return redirect("rip_user_registration")

    context = {
        'form': RipUserCreationForm()
    }

    return render(request, 'rip_auth/registration.html', context)

@csrf_protect
def login_user(request):
    if str(request.user) is not "AnonymousUser":
        print(request.user)
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = RipUserLoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        print(username)
        print(password)

        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return redirect("rip_user_login")

    context = {
        'form': RipUserLoginForm()
    }

    return render(request, 'rip_auth/login.html', context)

def logout_user(request):
    if not request.user:
        return HttpResponseRedirect('/')

    logout(request)
    return redirect("dday_list_view")