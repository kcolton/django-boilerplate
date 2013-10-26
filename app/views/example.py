from decimal import Decimal
from django import forms
from django.contrib import messages
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.utils.datetime_safe import datetime
from lib.django.views.decorators import html_view, json_view, csv_attachment_view
from django.views.decorators.cache import cache_control


@cache_control(public=True, s_maxage=3600, max_age=3600)
@html_view(template='example/index.tpl')
def index(request):
    return {}


@html_view(template='example/form.tpl')
def form_example(request):

    class MyForm(forms.Form):
        CHOICE_ONE = 1
        CHOICE_TWO = 2
        CHOICE_THREE = 3

        CHOICES = (
            (CHOICE_ONE, 'Choice One'),
            (CHOICE_TWO, 'Choice Two'),
            (CHOICE_THREE, 'Choice Three'),
        )

        example_char = forms.CharField(initial='Some text',
                                       help_text="This is some text to help you. <a href=\"http://google.com\">Need more help</a>")
        example_choice = forms.ChoiceField(choices=CHOICES, initial=CHOICE_ONE)
        example_date = forms.DateField(initial=datetime.now())
        example_datetime = forms.DateTimeField(initial=datetime.now(),
                                               help_text="Some tip for this date field")
        example_decimal = forms.DecimalField(initial=Decimal('42.22'))
        example_email = forms.EmailField(initial='myemail@email.com')
        example_required_bool = forms.BooleanField(initial=True)
        example_bool = forms.BooleanField(required=False, initial=False)
        example_radios = forms.ChoiceField(choices=CHOICES, initial=CHOICE_TWO, widget=forms.RadioSelect)
        example_checks = forms.MultipleChoiceField(choices=CHOICES, initial=[CHOICE_TWO, CHOICE_THREE], widget=forms.CheckboxSelectMultiple)
        example_file = forms.FileField(required=False)
        example_float = forms.FloatField(initial=42.22)
        example_image = forms.ImageField(required=False)
        example_integer = forms.IntegerField(initial=3)
        example_multi = forms.MultipleChoiceField(choices=CHOICES, initial=[CHOICE_ONE, CHOICE_TWO])

        example_hidden = forms.CharField(initial='I am hiding', widget=forms.HiddenInput)

        def clean(self):
            cleaned_data = super(MyForm, self).clean()
            if cleaned_data['example_bool']:
                raise forms.ValidationError('Tricked you! You do not really want to have example bool checked.')
            return cleaned_data

    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Form saved successfully')
            return HttpResponseRedirect(request.get_full_path())
        else:
            messages.error(request, 'Some required fields are missing or invalid. Details below.')
    else:
        form = MyForm()

    return {
        'form': form
    }


@html_view(template='example/messages.tpl')
def messages_example(request):
    messages.set_level(request, messages.DEBUG)
    messages.debug(request, 'This is a debug message')
    messages.info(request, 'This is an informational message. It also happens to be a decently long one just to see how everything looks when it has to wrap to multiple lines')
    messages.success(request, '<strong>Great success!</strong> Whatever you did seems to have worked out!')
    messages.warning(request, 'Better watch out! This is a warning.')
    messages.error(request, 'Bad bad bad! Something really awful happened!')
    messages.add_message(request, 8000, 'Custom message level')
    return {}


def redirect_internal(request):
    messages.success(request, 'You have been redirected successfully!')
    return HttpResponseRedirect(urlresolvers.reverse('messages_example'))


def redirect_external(request):
    return HttpResponseRedirect('http://www.youtube.com/watch?v=GP5D2apU2SE')


@cache_control(public=True, s_maxage=3600, max_age=3600)
@html_view(template='example/foo.tpl')
def foo(request):
    return {}


@cache_control(public=True, s_maxage=3600, max_age=3600)
@html_view(template='example/bar.tpl')
def bar(request):
    return {}


@json_view
def json(request):
    return dict(foo='bar')


@csv_attachment_view(filename='things.csv')
def csv_download(request):
    rows = [
        ['Column One', 'Column Two', 'Column Three'],
        ['Foo', 'Bar', 'Baz'],
        ['Hamburger', 'Hot Dog', 'Bacon'],
        ['Beer', 'Wine', 'Whiskey']
    ]

    return rows

