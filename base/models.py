from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    sName = models.CharField(max_length=20)
    age = models.FloatField()


    def __str__(self):
        return self.sName
    
class Teacher(models.Model):
    id = models.BigAutoField(primary_key=True)
    tName = models.CharField(max_length=20)
    age = models.FloatField()


    def __str__(self):
        return self.tName
