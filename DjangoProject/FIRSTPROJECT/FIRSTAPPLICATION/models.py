from django.db import models
import random
import string
# Create your models here.

def random_str():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(10))

def random_id():
    return str(random.randint(10000,99000))

class Employee(models.Model):
    name = models.CharField(max_length=50 , default = random_str)
    emp_id = models.CharField(max_length=10, default = random_id)
    contact = models.CharField(max_length=10, default = random_str)
    address = models.CharField(max_length=50, default = random_str)
