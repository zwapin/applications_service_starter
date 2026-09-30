# IMPORTING THIRD PARTY PACKAGES
from rest_framework.request import Request
from rest_framework.response import Response

# IMPORTING KLAARYO PACKAGES
from mini_kit.views import BaseApiView

# IMPORTING LOCAL PACKAGES
from rest_apis.managers import StoreApiManager
from rest_apis.serializers import StoreSerializerModel


class StoresApiView(BaseApiView):
    manager_class = StoreApiManager

    def get(self, request: Request) -> Response:
        return self.respond_list(self.manager.list_stores(), StoreSerializerModel)

    def post(self, request: Request) -> Response:
        return self.respond_created(self.manager.create_store(request.data), StoreSerializerModel)


class SingleStoreApiView(BaseApiView):
    manager_class = StoreApiManager

    def get(self, request: Request, store_pk: int) -> Response:
        return self.respond_item(self.manager.get_store(store_pk), StoreSerializerModel)
