from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models import EmailField, TextField, BooleanField
from rest_framework.serializers import ModelSerializer


class User(AbstractBaseUser, PermissionsMixin):

    email = EmailField(null=False, unique=True)
    firstname = TextField(null=False)
    lastname = TextField(null=False)
    is_superuser = BooleanField(null=False, default=False)
    is_active = BooleanField(null=False, default=False)

    USERNAME_FIELD = 'email'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        excludes = ['password']
