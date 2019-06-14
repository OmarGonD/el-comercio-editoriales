from django.db import models

# Create your models here.

class Editorial(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=40)
    body = models.CharField(max_length=100)
    url = models.CharField(max_length=400)
    image = models.CharField(max_length=400)

    def __str__(self):
        return f"Editorial con id:  #{self.id}"

    def __repr__(self):
        return f"Editorial con id:  #{self.id}"
