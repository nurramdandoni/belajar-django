from django.db import models

# Create your models here.

class About(models.Model):
    preface = models.CharField(max_length=100)
    detail = models.CharField(max_length=255,null=True)
    created_by = models.IntegerField(max_length=11,default='',null=True)
    created_at = models.DateTimeField(default='',null=True)
    updated_by = models.IntegerField(max_length=11,default='',null=True)
    updated_at = models.DateTimeField(default='',null=True)
    
    @classmethod
    def get_all_data(self):
        data = self.objects.all().values()
        return data
