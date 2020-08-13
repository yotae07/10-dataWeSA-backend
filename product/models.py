from django.db import models

class Group(models.Model):
    group      = models.CharField(max_length=200)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'groups'

class Occupation(models.Model):
    name       = models.CharField(max_length=200)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'occupations'

class Year(models.Model):
    year       = models.CharField(max_length=20)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'years'

class Race(models.Model):
    race       = models.CharField(max_length=200)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'races'

class Chart(models.Model):
    occupation = models.ForeignKey(Occupation, on_delete=models.SET_NULL, null=True)
    year       = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    group      = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    people     = models.IntegerField()
    salary     = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'charts'

class Graph(models.Model):
    race       = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)
    year       = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    people     = models.IntegerField()
    salary     = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'graphs'

class Product(models.Model):
    name       = models.CharField(max_length=100)
    image      = models.TextField()
    url        = models.TextField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
