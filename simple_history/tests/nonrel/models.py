from django.db import models
from simple_history.models import HistoricalRecords


class NonRelRelated(models.Model):
    pass


class NonRel(models.Model):
    related = models.ForeignKey(NonRelRelated)
    history = HistoricalRecords()
