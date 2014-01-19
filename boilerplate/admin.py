from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from . import forms
from django.contrib.auth.models import Group


class UserAdmin(DefaultUserAdmin):
    # The forms to add and change user instances
    form = forms.UserChangeForm
    add_form = forms.UserCreationForm

    # The fields that will be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that references specific fields on auth.User which don't exist here
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        (None,              {'fields': ('email', 'password')}),
        ('Permissions',     {'fields': ('is_staff',)}),
        ('Important Dates', {'fields': ('last_login',)}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)

    filter_horizontal = ()


# Unregister Group from admin app because we aren't using permissions
try:
    admin.site.unregister(Group)
except admin.site.NotRegistered:
    pass