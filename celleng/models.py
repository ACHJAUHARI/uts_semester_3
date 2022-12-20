from django.db import models

# Create your models here.
class Ceo(models.Model):
    name = models.CharField(max_length=50)
    keterangan = models.TextField()
    
    def __str__(self):
        return self.name
    
class Group(models.Model):
    member = models.CharField(max_length=30)
    lahir = models.CharField(max_length=50)
    alamat = models.CharField(max_length=30)
    status =models.TextField()
    
    def __str__(self):
        return self.member