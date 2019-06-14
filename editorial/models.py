from django.db import models

# Create your models here.

class Editorial(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=400)
    url = models.CharField(max_length=600)
    image = models.CharField(max_length=600)

    def __str__(self):
        return f"Editorial con id:  #{self.id}"

    def __repr__(self):
        return f"Editorial con id:  #{self.id}"
