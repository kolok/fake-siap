from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("operations:index"))
    # test si authentifié, si oui, rediriger vers convention/index...
    return render(request, "index.html")
