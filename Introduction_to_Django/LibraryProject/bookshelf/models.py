from django.db import models

class Book(models.Model):
    title = models.CharField (max_length=200)
    aur=thor = models.CharField (max_length=100)
    publication_year = models.IntegerField ()

    def __str__(self):
        return self.title