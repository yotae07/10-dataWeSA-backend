from django.db import models

from daily.models import State

class EconomicStatus(models.Model):
    state                     = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    is_deleted                = models.BooleanField(default=False)
    created_at                = models.DateTimeField(auto_now_add=True)
    updated_at                = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.state.name

    class Meta:
        db_table = 'economic_status'

class Claim(models.Model):
    economic         = models.ForeignKey(EconomicStatus, on_delete=models.SET_NULL, null=True)
    initial_claims   = models.IntegerField()
    continued_claims = models.IntegerField()
    is_deleted       = models.BooleanField(default=False)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.economic.state.name

    class Meta:
        db_table = 'claims'

class EmploymentStatus(models.Model):
    economic                  = models.ForeignKey(EconomicStatus, on_delete=models.SET_NULL, null=True)
    covered_employment        = models.FloatField()
    insured_unemployment_rate = models.FloatField()
    is_deleted                = models.BooleanField(default=False)
    created_at                = models.DateTimeField(auto_now_add=True)
    updated_at                = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.economic.state.name

    class Meta:
        db_table = 'employment_status'
