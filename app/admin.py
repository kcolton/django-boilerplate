from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from django_boilerplate.admin import UserAdmin


# Register our custom user object with admin app
admin.site.register(get_user_model(), UserAdmin)

# Unregister Group from admin app because we aren't using permissions
try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    print "Groups not registered. All good"
    pass