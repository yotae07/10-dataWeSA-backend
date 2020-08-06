from django.db import models

class State(models.Model):
    name        = models.CharField(max_length=256)
    populations = models.IntegerField()
    is_deleted  = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'states'

class Test(models.Model):
    state      = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    count      = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.state.name

    class Meta:
        db_table = 'tests'

class TestResult(models.Model):
    test                 = models.ForeignKey(Test, on_delete=models.CASCADE)
    confirmed_growth     = models.IntegerField(null=True)
    confirmed            = models.IntegerField()
    confirmed_per_capita = models.DecimalField(max_digits=10, decimal_places=2)
    positive_percent     = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted           = models.BooleanField(default=False)
    created_at           = models.DateTimeField(auto_now_add=True)
    updated_at           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.state.name

    class Meta:
        db_table = 'test_results'

class HospitalStatus(models.Model):
    state        = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    hospitalized = models.IntegerField(null=True)
    death        = models.IntegerField()
    is_deleted   = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.state.name

    class Meta:
        db_table = 'hospital_status'

class Graph(models.Model):
    state        = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    trend_graph  = models.TextField()
    gap_graph    = models.TextField()
    is_deleted   = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.state.name

    class Meta:
        db_table = 'daily_graph'
