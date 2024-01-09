from django.db import models

# Create your models here.


class Departments(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()


    def __str__(self):
        return self.dep_name   
    
class Doctor(models.Model):
    doc_name=models.CharField(max_length=255)
    doc_spec=models.CharField(max_length=255)
    doc_image=models.ImageField(upload_to='doctors')
    dep_name=models.ForeignKey(Departments,on_delete=models.CASCADE)

    def __str__(self):
        return self.doc_name  