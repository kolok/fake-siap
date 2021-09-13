import datetime
import random
from django.test import TestCase
from core.tests import utils

from programmes.models import (
    Programme,
    Lot,
    LogementEDD,
    Logement,
    Financement,
    TypologieLogement,
    TypologieAnnexe,
    TypologieStationnement,
    TypeStationnement,
    Annexe,
)

def params_logement(index):
    if index<=10:
        return TypologieLogement.T1, 0.9, 30, 0, 0, 30
    if index<=20:
        return TypologieLogement.T2, 1., 40, 5, 2.5, 42.5
    if index<=30:
        return TypologieLogement.T3, 1.1, 55, 10, 5, 60
    if index<=40:
        return TypologieLogement.T4, 1.1, 80, 20, 10, 90
    return TypologieLogement.T5, 0.9, 110, 28, 12, 122

class BailleurModelsTest(TestCase):
    # pylint: disable=E1101 no-member
    @classmethod
    def setUpTestData(cls):
        bailleur = utils.create_bailleur()
        programme = Programme.objects.create(
            nom="3F",
            bailleur = bailleur,
            code_postal = "75007",
            ville = "Paris",
            adresse = "22 rue segur",
            departement = 75,
            nb_logements = 100,
            numero_galion = "12345",
            annee_gestion_programmation = 2018,
            zone_123 = 3,
            zone_abc = 'B1',
            surface_utile_totale = 5243.21,
            nb_locaux_commerciaux = 5,
            nb_bureaux = 25,
            autre_locaux_hors_convention = "quelques uns",
            vendeur = "identité du vendeur",
            acquereur = "identité de l'acquéreur",
            permis_construire = "123 456 789 ABC",
            date_achevement_previsible = datetime.date.today() + datetime.timedelta(days=365),
            date_achat = datetime.date.today() - datetime.timedelta(days=365),
            date_achevement = datetime.date.today() + datetime.timedelta(days=465),
        )

        count = 0
        for financement in [Financement.PLAI,Financement.PLUS]:
            count += 1
            lot = Lot.objects.create(
                numero = count,
                bailleur = bailleur,
                programme = programme,
                financement = financement,
            )
            for index in range(50):
                typologie, coef, sh, sa, sar, su = params_logement(index)
                LogementEDD.objects.create(
                    designation = ("A" if financement == Financement.PLAI else "B") + str(index),
                    bailleur = bailleur,
                    programme = programme,
                    financement = financement,
                    typologie = typologie,
                )
                logement = Logement.objects.create(
                    designation = ("A" if financement == Financement.PLAI else "B") + str(index),
                    bailleur = bailleur,
                    lot = lot,
                    typologie = typologie,
                    surface_habitable = sh,
                    surface_annexes = sa,
                    surface_annexes_retenue = sar,
                    surface_utile = su,
                    loyer_par_metre_carre = 5.1,
                    coeficient = coef,
                    loyer = su*coef*5.1,
                )
                if sa > 0:
                    shsr = sar - sa
                    Annexe.objects.create(
                        bailleur = bailleur,
                        logement = logement,
                        typologie = TypologieAnnexe.TERRASSE,
                        surface_hors_surface_retenue = shsr,
                        loyer_par_metre_carre = 0.5,
                        loyer = shsr*0.5,
                    )
            TypeStationnement.objects.create(
                bailleur = bailleur,
                lot = lot,
                typologie = TypologieStationnement.PLACE_STATIONNEMENT,
                nb_stationnements = random.randint(1,10),
                loyer = random.randint(40, 75),
            )
            TypeStationnement.objects.create(
                bailleur = bailleur,
                lot = lot,
                typologie = TypologieStationnement.GARAGE_AERIEN,
                nb_stationnements = random.randint(1,10),
                loyer = random.randint(40, 75),
            )

    def test_object_str(self):
        programme = Programme.objects.order_by('-uuid').first()
        expected_object_name = f"{programme.nom}"
        self.assertEqual(str(programme), expected_object_name)

        logement_edd = LogementEDD.objects.order_by('-uuid').first()
        expected_object_name = f"{logement_edd.designation}"
        self.assertEqual(str(logement_edd), expected_object_name)

        lot = Lot.objects.order_by('-uuid').first()
        expected_object_name = f"{lot.programme.nom} - {lot.financement}"
        self.assertEqual(str(lot), expected_object_name)

        logement = Logement.objects.order_by('-uuid').order_by('-uuid').first()
        expected_object_name = f"{logement.designation}"
        self.assertEqual(str(logement), expected_object_name)

        annexe = Annexe.objects.order_by('-uuid').first()
        expected_object_name = f"{annexe.typologie} - {annexe.logement.designation}"
        self.assertEqual(str(annexe), expected_object_name)

        stationnement = TypeStationnement.objects.order_by('-uuid').first()
        expected_object_name = (f"{stationnement.typologie} - " +
            f"{stationnement.lot.programme.nom} - {stationnement.lot.financement}")
        self.assertEqual(str(stationnement), expected_object_name)


    def test_properties(self):
        logement = Logement.objects.order_by('uuid').first()
        self.assertEqual(logement.designation, logement.d)
        self.assertEqual(logement.typologie, logement.t)
        self.assertEqual(logement.surface_habitable, logement.sh)
        self.assertEqual(logement.surface_annexes, logement.sa)
        self.assertEqual(logement.surface_annexes_retenue, logement.sar)
        self.assertEqual(logement.surface_utile, logement.su)
        self.assertEqual(logement.loyer_par_metre_carre, logement.lpmc)
        self.assertEqual(logement.coeficient, logement.c)
        self.assertEqual(logement.loyer, logement.l)

        annexe = Annexe.objects.order_by('uuid').first()
        self.assertEqual(annexe.typologie, annexe.t)
        self.assertEqual(annexe.logement, annexe.lgt)
        self.assertEqual(annexe.surface_hors_surface_retenue, annexe.shsr)
        self.assertEqual(annexe.loyer_par_metre_carre, annexe.lpmc)
        self.assertEqual(annexe.loyer, annexe.l)

        stationnement = TypeStationnement.objects.order_by('uuid').first()
        self.assertEqual(stationnement.loyer, stationnement.l)
        self.assertEqual(stationnement.typologie, stationnement.t)
        self.assertEqual(stationnement.nb_stationnements, stationnement.nb)