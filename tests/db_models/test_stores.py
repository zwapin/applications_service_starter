# IMPORTING THIRD PARTY PACKAGES
from django.test import TestCase

# IMPORTING LOCAL PACKAGES
from django_db_models.models import StoreModel


class StoreModelTest(TestCase):

    def test_for_team_returns_only_the_rows_of_that_team(self):
        own_store = StoreModel.objects.create(team_pk=1, name="Trattoria Centrale", city="Roma")
        StoreModel.objects.create(team_pk=2, name="Market Lingotto", city="Torino")

        self.assertQuerySetEqual(StoreModel.for_team(1), [own_store])
