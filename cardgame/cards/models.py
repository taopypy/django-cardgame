from django.db import models

# Create your models here.
class Card(models.Model):
    CHOICES=(("TE","Terra"),("FO","Fogo"),("AG","Agua"),("AR","Ar"),("SA","Sagrado"),("DE","Demoniaca"))
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="cards")
    power = models.IntegerField(default=1)
    life = models.IntegerField(default=1)
    mana = models.IntegerField(default=1)
    element = models.CharField(max_length=2, choices=CHOICES, db_index=True)

    def __unicode__(self):
        return self.name

class Effect(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)


class Magia(models.Model):
    effect = models.ForeignKey(Effect)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)





