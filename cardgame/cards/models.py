from django.db import models


class Card(models.Model):
    CHOICES = (("TE", "Terra"),
               ("FO", "Fogo"),
               ("AG", "Agua"),
               ("AR", "Ar"),
               ("SA", "Sagrado"),
               ("DE", "Demoniaca"))

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="cards/%Y/%m/%d/")
    power = models.IntegerField(default=1)
    life = models.IntegerField(default=1)
    mana = models.IntegerField(default=1)
    element = models.CharField(max_length=2, choices=CHOICES, db_index=True)

    def __unicode__(self):
        return self.name
