from django.db import models

from daily.models import State

class Place(models.Model):
    name       = models.CharField(max_length=256)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'places'

class Mobility(models.Model):
    state      = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    place      = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    visit_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.state.name

    class Meta:
        db_table = 'mobilities'
