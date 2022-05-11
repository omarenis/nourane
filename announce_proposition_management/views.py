from django.urls import path
from announce_proposition_management.models import LocalisationSerializer, CategorySerializer, AnnounceSerializer
from announce_proposition_management.services import LocalisationService, CategoryService, AnnounceService
from common.views import ViewSet


class LocalisationViwSet(ViewSet):
    def __init__(self, serializer_class=LocalisationSerializer, service=LocalisationService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)


class CategoryViewSet(ViewSet):
    def __init__(self, serializer_class=CategorySerializer, service=CategoryService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)


class AnnounceViewSet(ViewSet):
    def __init__(self, serializer_class=AnnounceSerializer, service=AnnounceService(), **kwargs):
        super().__init__(serializer_class, service, **kwargs)


localisations, localisation = LocalisationViwSet().get_urls()
categories, category = CategoryViewSet().get_urls()
announces, announce = AnnounceViewSet().get_urls()

urlpatterns = [
    path('localisations', localisations),
    path('localisations/<int: pk>', localisation),
    path('categories', categories),
    path('categories/<int: pk>', categories),
    path('announces', announces),
    path('announces/<int:pk>', announce)
]
