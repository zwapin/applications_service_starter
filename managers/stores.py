# IMPORTING THIRD PARTY PACKAGES
from django.apps import apps
from django.db.models import QuerySet

# IMPORTING LOCAL PACKAGES
from managers.errors import StoreNotFoundError


class StoreManager:
    """Domain logic of the stores of one team: plain data in, model instances out."""

    def __init__(self, team_pk: int):
        self._team_pk = team_pk

    def list_stores(self) -> QuerySet:
        return self._store_model().for_team(self._team_pk).order_by("name")

    def get_store(self, store_pk: int) -> "StoreModel":
        store = self.list_stores().filter(pk=store_pk).first()
        if store is None:
            raise StoreNotFoundError()
        return store

    def create_store(self, name: str, city: str) -> "StoreModel":
        return self._store_model().objects.create(team_pk=self._team_pk, name=name, city=city)

    @staticmethod
    def _store_model() -> type["StoreModel"]:
        return apps.get_model("django_db_models", "StoreModel")
