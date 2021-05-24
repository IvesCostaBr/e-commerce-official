from django.db import models
from django.contrib.auth.models import User


class Adress(models.Model):
    rua = models.CharField(max_length=80)
    bairro = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    cep = models.CharField(max_length=80)
    complemento = models.CharField(max_length=80)
    reference_point = models.CharField(max_length=60)

class Costumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Adress, on_delete=models.PROTECT, blank=True, null=True)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField(auto_now_add=False)


    def __str__(self):
        return str(self.user.username) + ' ' + str(self.cpf)





