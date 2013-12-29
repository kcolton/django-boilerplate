import boilerplate.models


class User(boilerplate.models.User):
    class Meta:
        db_table = 'users'