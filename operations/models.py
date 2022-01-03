import uuid

from django.db import models
from django.urls import reverse

class Financement(models.TextChoices):
    PLUS = "PLUS", "PLUS"
    PLAI = "PLAI", "PLAI"
    PLAI_ADP = "PLAI_ADP", "PLAI_ADP"
    PLUS_PLAI = "PLUS-PLAI", "PLUS-PLAI"
    PLS = "PLS", "PLS"


class TypeOperation(models.TextChoices):
    SANSOBJET = "SANSOBJET", "Sans Objet"
    NEUF = "NEUF", "Construction Neuve"
    ACQUIS = "ACQUIS", "Acquisition-Amélioration"
    DEMEMBREMENT = "DEMEMBREMENT", "Démembrement"
    REHABILITATION = "REHABILITATION", "Réhabilitation"
    SANSTRAVAUX = "SANSTRAVAUX", "Sans travaux"
    USUFRUIT = "USUFRUIT", "Usufruit"
    VEFA = "VEFA", "VEFA"


class TypeHabitat(models.TextChoices):
    SANSOBJET = "SANSOBJET", "Sans Objet"
    INDIVIDUEL = "INDIVIDUEL", "Individuel"
    COLLECTIF = "COLLECTIF", "Collectif"


class Bailleur(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255)
    siret = models.CharField(max_length=14)
    capital_social = models.FloatField(null=True)
    adresse = models.CharField(max_length=255, null=True)
    code_postal = models.CharField(max_length=255, null=True)
    ville = models.CharField(max_length=255, null=True)
    signataire_nom = models.CharField(max_length=255, null=True)
    signataire_fonction = models.CharField(max_length=255, null=True)
    signataire_date_deliberation = models.DateField(null=True)
    operation_exceptionnelle = models.TextField(null=True)
    cree_le = models.DateTimeField(auto_now_add=True)
    mis_a_jour_le = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nom}"


class Administration(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    ville_signature = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nom


class Operation(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255)
    bailleur = models.ForeignKey(
        "Bailleur", on_delete=models.CASCADE, null=False
    )
    administration = models.ForeignKey(
        "Administration", on_delete=models.SET_NULL, null=True
    )
    code_postal = models.CharField(max_length=10, null=True)
    ville = models.CharField(max_length=255, null=True)
    adresse = models.CharField(max_length=255, null=True)
    numero_galion = models.CharField(max_length=255, null=True)
    annee_gestion_programmation = models.IntegerField(null=True)
    zone_123 = models.IntegerField(null=True)
    zone_abc = models.CharField(max_length=255, null=True)
    surface_utile_totale = models.DecimalField(
        max_digits=8, decimal_places=2, null=True
    )
    type_habitat = models.CharField(
        max_length=25,
        choices=TypeHabitat.choices,
        default=TypeHabitat.INDIVIDUEL,
    )
    type_operation = models.CharField(
        max_length=25,
        choices=TypeOperation.choices,
        default=TypeOperation.NEUF,
    )
    anru = models.BooleanField(default=False)
    nb_locaux_commerciaux = models.IntegerField(null=True)
    nb_bureaux = models.IntegerField(null=True)
    autres_locaux_hors_convention = models.TextField(null=True)
    date_achevement_previsible = models.DateField(null=True)
    cree_le = models.DateTimeField(auto_now_add=True)
    mis_a_jour_le = models.DateTimeField(auto_now=True)

    plai = models.BooleanField(default=False)
    plus = models.BooleanField(default=False)
    pls = models.BooleanField(default=False)
    autre = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('operations:operation_list')