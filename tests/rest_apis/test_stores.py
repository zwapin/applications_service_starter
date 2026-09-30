# IMPORTING THIRD PARTY PACKAGES
from rest_framework import status

# IMPORTING KLAARYO PACKAGES
from mini_kit.testing import KitAPITestCase

# IMPORTING LOCAL PACKAGES
from django_db_models.models import StoreModel

STORES_URL = "/api/v1/stores"


class StoresApiTest(KitAPITestCase):

    def setUp(self):
        self.store = StoreModel.objects.create(team_pk=1, name="Trattoria Centrale", city="Roma")
        StoreModel.objects.create(team_pk=2, name="Market Lingotto", city="Torino")

    def test_team_lists_only_its_own_stores(self):
        self.as_user(team_pk=1)

        response = self.client.get(STORES_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([store["name"] for store in response.json()["results"]], ["Trattoria Centrale"])

    def test_store_of_another_team_is_not_found(self):
        self.as_user(team_pk=2)

        response = self.client.get(f"{STORES_URL}/{self.store.pk}")

        self.assert_error(response, status.HTTP_404_NOT_FOUND, "store_not_found")

    def test_create_store_returns_the_created_store(self):
        self.as_user(team_pk=1)

        response = self.client.post(STORES_URL, {"name": "Bistrot Navigli", "city": "Milano"})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["name"], "Bistrot Navigli")

    def test_create_store_without_city_is_invalid_payload(self):
        self.as_user(team_pk=1)

        response = self.client.post(STORES_URL, {"name": "Bistrot Navigli"})

        self.assert_error(response, status.HTTP_400_BAD_REQUEST, "invalid_payload")
