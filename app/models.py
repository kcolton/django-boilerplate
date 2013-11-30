import django_boilerplate.models


class User(django_boilerplate.models.User):
    class Meta:
        db_table = 'users'