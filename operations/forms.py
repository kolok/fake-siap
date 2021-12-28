from django import forms
from django.core.exceptions import ValidationError
from django.forms import BaseFormSet, formset_factory
from core import forms_utils

from operations.models import (
    Operation,
)


class OperationForm(forms.Form):
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
    type_operation = forms.CharField(required=False)
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
