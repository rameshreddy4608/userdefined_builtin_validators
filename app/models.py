from django.db import models

# Create your models here.
from django.core import validators

class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    age=models.IntegerField()
    mobile=models.IntegerField()
    email=models.EmailField()
    


    def __str__(self):
        return str(self.sid)

class Course(models.Model):
    cid=models.IntegerField()
    sid=models.ForeignKey(Student,on_delete=models.CASCADE)
    cname=models.CharField(max_length=100)
    cTrainer=models.CharField(max_length=100)

    def __str__(self):
        return self.cname
    

