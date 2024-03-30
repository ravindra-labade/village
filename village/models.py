from django.db import models


class Village(models.Model):
    village_name = models.CharField(max_length=20)
    tehsil = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    population = models.IntegerField()
    village_head = models.CharField(max_length=20)


