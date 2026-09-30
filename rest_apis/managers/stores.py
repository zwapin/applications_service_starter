# IMPORTING STANDARD PACKAGES
from functools import cached_property

# IMPORTING THIRD PARTY PACKAGES
from django.db.models import QuerySet

# IMPORTING KLAARYO PACKAGES
from mini_kit.managers import BaseManager

# IMPORTING LOCAL PACKAGES
from managers import StoreManager
from rest_apis.serializers import StoreInputSerializer


class StoreApiManager(BaseManager):
    """REST side of the stores: validates the API input and delegates to the core StoreManager."""

    def list_stores(self) -> QuerySet:
        return self._store_manager.list_stores()

    def get_store(self, store_pk: int) -> "StoreModel":
        return self._store_manager.get_store(store_pk)

    def create_store(self, payload: dict) -> "StoreModel":
        data = self._validate_payload(StoreInputSerializer, payload)
        return self._store_manager.create_store(name=data["name"], city=data["city"])

    @cached_property
    def _store_manager(self) -> StoreManager:
        return StoreManager(team_pk=self.team_pk)
