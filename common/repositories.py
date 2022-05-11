from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, User
from django.db.models import Model


def set_password(password, _object):
    if isinstance(_object, AbstractUser) or \
            issubclass(_object.__class__, AbstractUser) or isinstance(_object, User) or \
            isinstance(_object.__class__, User) or isinstance(_object, AbstractBaseUser) or \
            isinstance(_object.__class__, AbstractBaseUser):
        _object.set_password(password)
        _object.save()
        return _object
    else:
        raise AttributeError("password only allowed for abstract clients or their children class")


class Repository(object):
    def __init__(self, model: Model or AbstractUser):
        self.model = model

    def list(self):
        return self.model.objects.all()

    def retrieve(self, _id: int):
        return self.model.objects.get(id=_id)

    def put(self, _id: int, data: dict):
        _object = self.model.objects.get(id=_id)
        if _object is None:
            return Exception('object not found')
        else:
            for i in data:
                if hasattr(_object, i) and getattr(_object, i) != data[i]:
                    setattr(_object, i, data[i])
            print(isinstance(_object.__class__, AbstractUser))
            _object = set_password(data.get('password'), _object)
        return _object

    def create(self, data: dict):

        _object = self.model.objects.create(**data)
        if isinstance(_object, Exception):
            return _object
        if data.get('password') is not None:
            _object = set_password(data.get('password'), _object)
        return _object

    def delete(self, _id):
        return self.model.objects.get(pk=_id).delete()

    def filter_by(self, data: dict):
        return self.model.objects.filter(**data)
