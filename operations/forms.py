from django import forms
from django.forms import ModelForm
from core import forms_utils

from operations.models import (
    Operation,
    TypeHabitat,
    TypeOperation,
)

class OperationForm(ModelForm):
  class Meta:
    model = Operation
    fields = ['nom', 'bailleur', 'administration', 'code_postal', 'ville',
    'adresse', 'numero_galion', 'annee_gestion_programmation', 'zone_123',
    'zone_abc', 'surface_utile_totale', 'type_habitat', 'type_operation',
    'date_achevement_previsible', 'nb_plai', 'nb_plus', 'nb_pls', 'nb_autre',]
    labels = {
        'nom': 'Nom',
        'bailleur': 'Entreprise bailleur (MOA)',
        'nb_plai': 'Nombre de logements PLAI',
        'nb_plus': 'Nombre de logements PLUS',
        'nb_pls': 'Nombre de logements PLS',
        'nb_autre': 'Nombre de logements Autre',
    }

class Operation2Form(forms.Form):
    object_name = "programme"

    uuid = forms.UUIDField(required=False)
    nom = forms.CharField(
        max_length=255,
        min_length=1,
        error_messages={
            "required": "Le nom du programme est obligatoire",
            "min_length": "Le nom du programme est obligatoire",
            "max_length": "Le nom du programme ne doit pas excéder 255 caractères",
        },
    )
    adresse, code_postal, ville = forms_utils.address_form_fields()
    nb_logements = forms.IntegerField(
        error_messages={
            "required": "Le nombre de logements à conventionner est obligatoire",
        },
    )
    type_habitat = forms.TypedChoiceField(required=False, choices=TypeHabitat.choices)
    type_operation = forms.TypedChoiceField(required=False, choices=TypeOperation.choices)
    anru = forms.BooleanField(required=False)
    nb_locaux_commerciaux = forms.IntegerField(required=False)
    nb_bureaux = forms.IntegerField(required=False)
    autres_locaux_hors_convention = forms.CharField(
        required=False,
        max_length=5000,
        error_messages={
            "max_length": "L'information ne doit pas excéder 5000 characters",
        },
    )
