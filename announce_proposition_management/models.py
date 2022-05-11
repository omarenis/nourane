# Create your models here.
from django.db.models import Model, TextField, ForeignKey, CASCADE, DateField, DateTimeField, SlugField, SET_NULL, \
    BooleanField
from django.forms import ImageField
from django.utils.timezone import now
from rest_framework.serializers import ModelSerializer


class Localisation(Model):
    governorate = TextField(null=False)
    region = TextField(null=False)
    zipCode = TextField(null=False)


class Category(Model):
    name = TextField(null=False)
    slug = SlugField(null=False)
    icon = ImageField(null=False)
    icon_path = TextField(null=False)


class Announce(Model):
    category = ForeignKey(to='Category', null=True, on_delete=SET_NULL)
    region = ForeignKey(to='Region', null=True, on_delete=SET_NULL)
    title = TextField(null=False)
    description = TextField(null=False)
    dateCreation = DateTimeField(null=False, default=now)
    user = ForeignKey(to='user_auth_management.User', on_delete=CASCADE, null=False)
    slug = SlugField(null=False)
    image = ImageField(null=False)


class Proposition(Model):
    user = ForeignKey(to='user_auth_management.User', on_delete=CASCADE, null=False)
    announce = ForeignKey(to='Announce', on_delete=CASCADE, null=False)
    dateCreation = DateField(null=False, default=now)
    details = TextField(null=True, default=None)
    isAccepted = BooleanField(null=False)


class LocalisationSerializer(ModelSerializer):
    class Meta:
        model = Localisation
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "_all__"


class AnnounceSerializer(ModelSerializer):
    class Meta:
        model = Announce
        fields = "__all__"


class PropositionSerializer(ModelSerializer):
    class Meta:
        model = Announce
        fields = "__all__"
