from django.db import models

# Create your models here.

class about(models.Model):
    preface = models.CharField(max_length=100)
    detail = models.CharField(max_length=255)
    created_by = models.IntegerField(max_length=11)
    created_at = models.DateTimeField()
    updated_by = models.IntegerField(max_length=11)
    updated_at = models.DateTimeField()
