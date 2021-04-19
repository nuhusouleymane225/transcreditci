"""
Definition of models.
"""

from django.db import models



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vehicule(models.Model):
    name = models.CharField(max_length=255)
    category_vehicule = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Category")
    slug = models.SlugField()
    details = models.TextField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PersonalData(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    number = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Commentaire(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    sujet = models.TextField()
    email = models.CharField(max_length=255)
    commentaire = models.TextField()

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=255)
    numero = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email




