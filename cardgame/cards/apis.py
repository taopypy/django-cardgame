from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import routers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card


class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer


card_router = routers.DefaultRouter()
card_router.register(r'card', CardViewSet)
