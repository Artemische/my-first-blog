from django.db import models
from random import randint

class Inform(models.Model):
    GROUP_CHICES = (
        ('10706117','10706117'),
        ('10703117', '10703117'),
        ('10703217', '10703217'),
    )
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    group = models.CharField(max_length=200, choices=GROUP_CHICES)
    task = models.IntegerField(default=0)