from django.db import models

class Synsets(models.Model):
    lemma = models.CharField(max_length=30)
    aspect = models.CharField(max_length=30)
    definition = models.CharField(max_length=150)
