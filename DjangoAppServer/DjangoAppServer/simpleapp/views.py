from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET


@login_required
@require_GET
def withauthapp(request):
    meta = request.META
    return render(request, "withauthapp.html", {'meta': meta, 'user': request.user})


@require_GET
def noauthapp(request):
    meta = request.META
    return render(request, "withauthapp.html", {'meta': meta, 'user': request.user})
