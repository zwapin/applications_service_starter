# IMPORTING THIRD PARTY PACKAGES
from django.test import TestCase

# IMPORTING LOCAL PACKAGES
from django_db_models.models import StoreModel
from managers import StoreManager, StoreNotFoundError


class StoreManagerTest(TestCase):

    def test_create_store_belongs_to_the_manager_team(self):
        store = StoreManager(team_pk=1).create_store(name="Bistrot Navigli", city="Milano")

        self.assertEqual(store.team_pk, 1)

    def test_store_of_another_team_is_not_found(self):
        store = StoreModel.objects.create(team_pk=1, name="Trattoria Centrale", city="Roma")

        with self.assertRaises(StoreNotFoundError):
            StoreManager(team_pk=2).get_store(store.pk)
