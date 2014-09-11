from django.conf.urls import patterns, include, url
from .apis import card_router


urlpatterns = patterns('',
                       url(r'^api/', include(card_router.urls)),
                       )
