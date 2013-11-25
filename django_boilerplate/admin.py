# Pretty much drop in from https://docs.djangoproject.com/en/1.5/topics/auth/customizing/

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

from .models import User


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all required
    fields, plus a repeated password"""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

    def save(self, commit=True):
        # Save the provided password in the hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields
    on the user, but replaces the password field with admin's
    password hash display fiedl"""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial['password']


class UserAdmin(DefaultUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

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

# Register our custom user object with admin app
admin.site.register(User, UserAdmin)

# Unregister Group from admin app because we aren't using permissions
try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    print "Groups not registered. All good"
    pass