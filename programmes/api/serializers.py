from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import serializers

from instructeurs.api.permissions import AdministrationPermission
from instructeurs.api.serializers import AdministrationSerializer
from instructeurs.models import Administration

from bailleurs.api.permissions import BailleurPermission
from bailleurs.models import Bailleur
from bailleurs.api.serializers import BailleurSerializer

from programmes.models import Programme


class ProgrammeSerializer(serializers.HyperlinkedModelSerializer):
    bailleur = BailleurSerializer(read_only=True)
    bailleur_uuid = serializers.CharField(write_only=True)
    administration = AdministrationSerializer(read_only=True)
    administration_uuid = serializers.CharField(write_only=True)

    class Meta:
        model = Programme
        fields = [
            "uuid",
            "nom",
            "bailleur",
            "bailleur_uuid",
            "administration",
            "administration_uuid",
            "code_postal",
            "ville",
            "adresse",
            "numero_galion",
            "annee_gestion_programmation",
            "zone_123",
            "zone_abc",
            "surface_utile_totale",
            "type_habitat",
            "type_operation",
            "anru",
            "nb_locaux_commerciaux",
            "nb_bureaux",
            "autres_locaux_hors_convention",
            "date_acte_notarie",
            "mention_publication_edd_volumetrique",
            "mention_publication_edd_classique",
            "permis_construire",
            "date_achevement_previsible",
            "date_achat",
            "date_achevement",
        ]
        read_only_fields = (
            "vendeur",
            "acquereur",
            "reference_notaire",
            "reference_publication_acte",
            "acte_de_propriete",
            "acte_notarial",
            "reference_cadastrale",
            "edd_volumetrique",
            "edd_classique",
        )

    def create(self, validated_data):
        """
        Create and return a new `Programme` instance, given the validated data.
        """
        validated_data = self._get_bailleur(validated_data)
        validated_data = self._get_administration(validated_data)
        return Programme.objects.create(**validated_data)

    def _get_bailleur(self, validated_data):
        if "bailleur_uuid" not in validated_data.keys():
            raise serializers.ValidationError(
                {
                    "bailleur_uuid": "L'identifiant unique est obligatoire pour créer le programme"
                }
            )
        bailleur_uuid = validated_data.pop("bailleur_uuid")
        try:
            bailleur = Bailleur.objects.get(uuid=bailleur_uuid)
            if not BailleurPermission.has_object_permission(
                self, self.context, self, bailleur
            ):
                raise PermissionDenied()
        except Bailleur.DoesNotExist as does_not_exist:
            raise Http404("bailleur non trouvé") from does_not_exist
        validated_data["bailleur"] = bailleur
        return validated_data

    def _get_administration(self, validated_data):
        if "administration_uuid" not in validated_data.keys():
            raise serializers.ValidationError(
                {
                    "administration_uuid": "L'identifiant unique est"
                    + " obligatoire pour créer le programme"
                }
            )
        administration_uuid = validated_data.pop("administration_uuid")
        try:
            administration = Administration.objects.get(uuid=administration_uuid)
            if not AdministrationPermission.has_object_permission(
                self, self.context, self, administration
            ):
                raise PermissionDenied()
        except Administration.DoesNotExist as does_not_exist:
            raise Http404("administration non trouvé") from does_not_exist
        validated_data["administration"] = administration
        return validated_data

    def update(self, instance, validated_data):
        """
        Update and return an existing `Programme` instance, given the validated data.
        """

        current_user = self.context.user
        if "bailleur_uuid" in validated_data.keys():
            bailleur_uuid = validated_data.pop("bailleur_uuid")
            try:
                instance.bailleur = Bailleur.objects.get(uuid=bailleur_uuid)
                if not BailleurPermission.has_object_permission(
                    self, self.context, self, instance.bailleur
                ):
                    raise PermissionDenied

                if instance.bailleur not in current_user.bailleurs():
                    raise PermissionDenied()
            except Bailleur.DoesNotExist as does_not_exist:
                raise Http404("bailleur non trouvé") from does_not_exist

        for field in [
            "nom",
            # "administration",
            "code_postal",
            "ville",
            "adresse",
            "numero_galion",
            "annee_gestion_programmation",
            "zone_123",
            "zone_abc",
            "surface_utile_totale",
            "type_habitat",
            "type_operation",
            "anru",
            "nb_locaux_commerciaux",
            "nb_bureaux",
            "autres_locaux_hors_convention",
            "date_acte_notarie",
            "mention_publication_edd_volumetrique",
            "mention_publication_edd_classique",
            "permis_construire",
            "date_achevement_previsible",
            "date_achat",
            "date_achevement",
        ]:
            setattr(
                instance, field, validated_data.get(field, getattr(instance, field))
            )

        instance.save()
        return instance