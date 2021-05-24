from django.db import models

# Create your models here.

class Produto(models.Model):
    titulo = models.CharField(max_length=90)
    bio = models.CharField(max_length=600, blank=True, null=True)
    image1 = models.ImageField(upload_to=f'produto-{titulo}/', blank=True, null=True)
    image2 = models.ImageField(upload_to=f'produto-{titulo}/', blank=True, null=True)
    image3 = models.ImageField(upload_to=f'produto-{titulo}/', blank=True, null=True)
    preco = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return  str(self.id) + ' ' + str(self.titulo)

class Caregoria(models.Model):
    pass