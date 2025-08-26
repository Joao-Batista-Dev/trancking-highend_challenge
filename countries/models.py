from django.db import models

class Assessment(models.Model):
    countrie = models.CharField(max_length=150)
    liked = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f"{self.pais} - {'curti' if self.curti else 'não curti'}"