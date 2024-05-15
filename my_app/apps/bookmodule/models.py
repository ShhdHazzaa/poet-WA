from django.db import models
from django.urls import reverse

class Poet(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Poem(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    poet = models.ForeignKey(Poet, on_delete=models.CASCADE, related_name='poems')
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
<<<<<<< HEAD
        return reverse('poem_detail', kwargs={'pk': self.pk})
=======
        return reverse('poem_detail', kwargs={'pk': self.pk})
>>>>>>> 7636508951104c9281f4c72fc7634805431a4d6a
