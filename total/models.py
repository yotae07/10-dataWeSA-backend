from django.db import models

class Total(models.Model):
    title      = models.CharField(max_length=256)
    value      = models.CharField(max_length=256)
    sub_title  = models.CharField(max_length=256)
    is_deleted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'total'
