from django.db import models

# Create your models here.
class ContactW (models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.name+" , "+self.email

class ContactPln (models.Model):
    
    bname=models.CharField(max_length=100)
    Mno=models.CharField(max_length=10)
    OPERATOR=models.CharField(max_length=100)
    PLAN=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.bname+" , "+self.Mno+","+self.OPERATOR+","+self.PLAN