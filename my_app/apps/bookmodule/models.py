from django.db import models

class Poet(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

class Poem(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    poet = models.ForeignKey(Poet, on_delete=models.CASCADE)
