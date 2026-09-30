# IMPORTING KLAARYO PACKAGES
from mini_kit.errors import NotFoundError


class StoreNotFoundError(NotFoundError):
    code = "store_not_found"
    default_message = "Store not found"
