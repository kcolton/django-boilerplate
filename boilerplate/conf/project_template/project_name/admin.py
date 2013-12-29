from django.contrib import admin
from django.contrib.auth import get_user_model
from boilerplate.admin import UserAdmin


admin.site.register(get_user_model(), UserAdmin)