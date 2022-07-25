from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_first_name = models.CharField(max_length=10)
    emp_last_name = models.CharField(max_length=10)
    eid=models.CharField(max_length=5)

    def __str__(self):
        return self.emp_first_name
        