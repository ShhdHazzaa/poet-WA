from django.db import models

class Poet(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    
    
    class Meta:
        app_label = 'bookmodule'
    def __str__(self):
        return self.name

class Poem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    poet = models.ForeignKey(Poet, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
