from django.db import models

# Create your models here.
class Module2Model(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    company = models.ForeignKey('module1.Company', on_delete=models.CASCADE, related_name='clients')
    
    def __str__(self):
        return self.name