from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from operations.models import Operation

# Create your views here.
@login_required
def index(request):
    operations = Operation.objects.all()

    return render(
        request,
        "operations/index.html",
        { "operations": operations },
    )
