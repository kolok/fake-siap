from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from operations.models import Operation
from operations.forms import OperationForm

# Create your views here.
@login_required
def index(request):
    operations = Operation.objects.all()

    return render(
        request,
        "operations/index.html",
        { "operations": operations },
    )


class OperationCreate(CreateView):
  model = Operation
  form_class = OperationForm
  def form_valid(self, form):    
    super(OperationCreate, self).form_valid(form)
    print('CREATE : Après form validate !!!')
    return redirect('operations:index')

class OperationUpdate(UpdateView):
  model = Operation
  form_class = OperationForm
  def form_valid(self, form):    
    super(OperationUpdate, self).form_valid(form)
    print('UPDATE : Après form validate !!!')
    return redirect('operations:index')

class OperationDelete(DeleteView):
  model = Operation
  success_url = reverse_lazy('operations:index')