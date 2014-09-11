from django.db import models
from django.contrib.auth.models import User
from cards.models import Card


class DeckManager(models.Manager):
    def create_default_decks(self):
        """
        Create default desks for users
        """
        return NotImplemented('Create default desks for users')


class Deck(models.Model):
    user = models.ForeignKey(User)
    description = models.TextField(null=True, blank=True)
    cards = models.ManyToManyField(Card)
    name = models.CharField(max_length=150)

    objects = DeckManager()

    def __str__(self):
        return self.name
