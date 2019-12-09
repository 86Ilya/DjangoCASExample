from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods, require_GET


from DjangoAuthServer.httpcodes import HTTP_BAD_REQUEST, HTTP_OK, HTTP_UNAUTHORIZED
from DjangoAuthServer.authapp.helpers import base, save_user_by_form
from DjangoAuthServer.authapp.forms import UserForm


User = get_user_model()


@require_http_methods(["GET", "POST"])
def login_view(request):
    context = base(request)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # r = redirect('/')
            # r['REMOTE_USER'] = username
            # return r
            return render(request, "login.html", context)
        else:
            context.update({'login_failed': True})
            return render(request, 'login.html', context, status=HTTP_UNAUTHORIZED)
    else:
        return render(request, "login.html", context)


@require_http_methods(["GET", "POST"])
def signup_view(request):
    context = base(request)
    status = HTTP_OK
    if request.method == "POST":
        signup_form, valid = save_user_by_form(request, context)
        context.update({'signup_form': signup_form})
        if valid:
            return render(request, 'signup_ok.html', {'error': None}, status=status)
        else:
            status = HTTP_BAD_REQUEST
    else:
        signup_form = UserForm
        context.update({'signup_form': signup_form})

    return render(request, 'signup.html', context, status=status)


@login_required
@require_GET
def logout_view(request):
    logout(request)
    return redirect('login')
