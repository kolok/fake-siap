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
    return render(
        request,
        "operations/operation_list.html",
        { "operations": operations},
    )

@login_required
def convention_list(request):
    convention_list = client_api.get_conventions()
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
    payload = {
      'nom' : form.cleaned_data["nom"],
      'bailleur_uuid' : f'{form.cleaned_data["bailleur"].apilos_uuid}',
      'administration_uuid' : f'{form.cleaned_data["administration"].apilos_uuid}',
      'code_postal' : form.cleaned_data["code_postal"],
      'ville' : form.cleaned_data["ville"],
      'adresse' : form.cleaned_data["adresse"],
      'numero_galion' : form.cleaned_data["numero_galion"],
      'annee_gestion_programmation' : form.cleaned_data["annee_gestion_programmation"],
      'zone_123' : form.cleaned_data["zone_123"],
      'zone_abc' : form.cleaned_data["zone_abc"],
      'surface_utile_totale' : f'{form.cleaned_data["surface_utile_totale"]}',
      'type_habitat' : form.cleaned_data["type_habitat"],
      'type_operation' : form.cleaned_data["type_operation"],
      'date_achevement_previsible' : f'{form.cleaned_data["date_achevement_previsible"]}',
#    'plai', 'plus', 'pls'
    }
    print(form.cleaned_data)
    print(self.object)
    programme = client_api.create_programme(payload)
    self.object.apilos_uuid = programme['uuid']
    self.object.save()

    if form.cleaned_data["plai"]:
      client_api.create_lot({
        'programme_uuid': programme['uuid'],
        'financement': 'PLAI',
        'nb_logements': 10
      })
    if form.cleaned_data["plus"]:
      client_api.create_lot({
        'programme_uuid': programme['uuid'],
        'financement': 'PLUS',
        'nb_logements': 10
      })
    if form.cleaned_data["pls"]:
      client_api.create_lot({
        'programme_uuid': programme['uuid'],
        'financement': 'PLS',
        'nb_logements': 10
      })

    print('CREATE PROGRAMME : Après form validate !!!')
    print(payload)
    print(self)
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