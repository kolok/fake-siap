from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from operations.models import Operation
from operations.forms import OperationForm
from operations.client_api import ClientAPI

client_api = ClientAPI()

# Create your views here.
@login_required
def operation_list(request):
    operations = Operation.objects.all()
    print('OP')
    return render(
        request,
        "operations/operation_list.html",
        { "operations": operations},
    )

@login_required
def convention_list(request):
    convention_list = client_api.get_conventions()
    print('CONV')
    return render(
        request,
        "operations/convention_list.html",
        { "conventions": convention_list},
    )


class OperationCreate(CreateView):
  model = Operation
  form_class = OperationForm
  def form_valid(self, form):    
    super(OperationCreate, self).form_valid(form)
    print('CREATE : Après form validate !!!')
    return redirect('operations:operation_list')

class OperationUpdate(UpdateView):
  model = Operation
  form_class = OperationForm
  def form_valid(self, form):    
    super(OperationUpdate, self).form_valid(form)
    print('UPDATE : Après form validate !!!')
    return redirect('operations:operation_list')

class OperationDelete(DeleteView):
  model = Operation
  success_url = reverse_lazy('operations:operation_list')