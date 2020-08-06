from django.db import models

from daily.models import State

class Bed(models.Model):
    state             = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, related_name='beds')
    beds_per_thousand = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted        = models.BooleanField(default=False)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.state.name

    class Meta:
        db_table = 'beds'

class Icu(models.Model):
    state            = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    total            = models.IntegerField()
    total_per_capita = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted       = models.BooleanField(default=False)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.state.name

    class Meta:
        db_table = 'icu'
