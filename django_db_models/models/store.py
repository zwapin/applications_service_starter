# IMPORTING THIRD PARTY PACKAGES
from django.db import models

# IMPORTING KLAARYO PACKAGES
from mini_kit.models import TeamScopedModel


class StoreModel(TeamScopedModel):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = "store"
        verbose_name_plural = "stores"

    def __str__(self) -> str:
        return f"{self.name} ({self.city})"

    def __repr__(self) -> str:
        return f"<StoreModel pk={self.pk} team_pk={self.team_pk} name={self.name!r}>"
