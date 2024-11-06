from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('musician-detail', kwargs={'musician_id': self.id})
    

class Music(models.Model):
        date = models.DateField()
        music_name = models.CharField(max_length=100)
        link = models.URLField(max_length=200, null=True, blank=True)
        
        musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
        def __str__(self):
            return self.music_name
        
        class Meta:
            ordering = ['-date']