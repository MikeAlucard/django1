from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuarios(models.Model):
	id_persona = models.OneToOneField(User, related_name='id_persona')
	sexo = models.BooleanField(default=True)
