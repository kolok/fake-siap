import uuid

from django.db import models
from django.urls import reverse

from core.models import IngestableModel

class Bailleur(IngestableModel):
    pivot= 'siret'
    mapping= {
        'nom': 'MOA (nom officiel)',
        'siret' : 'MOA (code SIRET)',
        'adresse': 'MOA Adresse 1',
        'code_postal' : 'MOA Code postal',
        'ville' : 'MOA Ville',
    }

    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255)
    siret = models.CharField(max_length=14)
    capital_social = models.CharField(max_length=255, null=True)
    adresse = models.CharField(max_length=255, null=True)
    code_postal = models.CharField(max_length=255, null=True)
    ville = models.CharField(max_length=255, null=True)
    dg_nom = models.CharField(max_length=255, null=True)
    dg_fonction = models.CharField(max_length=255, null=True)
    dg_date_deliberation = models.DateField(null=True)
    operation_exceptionnelle = models.TextField(null=True)

    cree_le = models.DateTimeField(auto_now_add=True)
    mis_a_jour_le = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("bailleurs:details", args=[str(self.uuid)])
