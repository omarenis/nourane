from .repositories import Repository


def validate_data(data, fields):
    for i in fields:
        if data.get(i) is None and fields[i].get('required') is True:
            return ValueError(f'{i} must not be null')
    return data


class Service(object):

    def __init__(self, repository: Repository, fields: dict):
        self.repository = repository
        self.fields = fields

    def list(self):
        return self.repository.list()

    def retrieve(self, _id: int):
        return self.repository.retrieve(_id=_id)

    def create(self, data: dict):
        for i in self.fields:
            if data.get(i) is None and self.fields[i].get('required') is True:
                return ValueError(f'{i} must not be null')
        return self.repository.create(data)

    def put(self, _id: int, data: dict):
        return self.repository.put(_id=_id, data=data)

    def delete(self, _id: int):
        return self.repository.delete(_id)

    def filter_by(self, data: dict):
        filter_params = {}
        for i in data:
            if self.fields.get(i) is not None and self.fields.get(i).get('type') == 'text':
                filter_params[f'{i}__contains'] = data[i]
            filter_params[i] = data[i]
        return self.repository.filter_by(data=filter_params)
