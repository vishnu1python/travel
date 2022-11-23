from django.db import models

class spot(models.Model):
    Place = models.CharField(max_length=250)
    Image = models.ImageField(upload_to='pics')
    Description = models.TextField()
    
    
class teams(models.Model):
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=250)
    desc = models.TextField()
    


    def __str__(self):
        return self.name
        