from django.utils.text import slugify
from announce_proposition_management.models import Localisation, Category, Proposition
from common.repositories import Repository
from common.services import Service

LOCALISATION_FIELDS = {
    'governorate': {'type': 'text', 'required': True},
    'region': {'type': 'text', 'required': True},
    'zipCode': {'type': 'text', 'required': True}
}

CATEGORY_FIELDS = {
    'name': {'type': 'text', 'required': True},
    'slug': {'type': 'qlug', 'required': True},
    'icon': {'type': 'file', 'required': True},
    'icon_path': {'type': 'text', 'required': False}
}

ANNOUNCE_FIELDS = {
    'category_id': {'type': 'integer', 'required': True},
    'region': {'type': 'text', 'required': True},
    'title': {'type': 'text', 'required': True},
    'description': {'type': 'text', 'required': True},
    'dateCreation': {'type': 'datetime', 'required': True},
    'user_id': {'type': 'integer', 'required': True},
    'slug': {'type': 'slug', 'required': False},
    'image': {'type': 'file', 'required': True}
}

PROPOSITION_FIELDS = {
    'user_id': {'type': 'integer', 'required': True},
    'announce_id': {'type': 'integer', 'required': True},
    'dateCreation': {'type': 'datetime', 'required': True},
    'isAccepted': {'type': 'boolean', 'required': True},
    'details': {'type': 'text', 'required': True}
}


class LocalisationService(Service):

    def __init__(self, repository=Repository(model=Localisation)):
        super().__init__(repository, LOCALISATION_FIELDS)


class CategoryService(Service):

    def __init__(self, repository=Repository(model=Category)):
        super().__init__(repository, CATEGORY_FIELDS)

    def create(self, data):
        user = super().create(data)
        if isinstance(user, Exception):
            return user
        user.slug = slugify(str(user.id) + data['title'])
        user.save()
        return user


class AnnounceService(Service):

    def __init__(self, repository=Repository(model=Category)):
        super().__init__(repository, ANNOUNCE_FIELDS)

    def create(self, data):
        announce = super().create(data)
        announce.slug = slugify(str(announce.id) + data['title'])
        announce.save()
        return announce

    def put(self, _id: int, data: dict):
        announce = super().put(_id, data)
        announce.slug = slugify(str(announce.id) + data['title'])
        announce.save()
        return announce


class PropositionService(Service):

    def __init__(self, repository=Repository(model=Proposition)):
        super().__init__(repository, PROPOSITION_FIELDS)
