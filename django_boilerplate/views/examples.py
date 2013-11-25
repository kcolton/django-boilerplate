from decimal import Decimal
import logging
import warnings

from django import forms
from django.contrib import messages
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.utils.datetime_safe import datetime
from django.views.decorators.cache import cache_control
from django_hijax.view_decorators import set_title

from ..models import User
from ..django_components.views.decorators import html_view, json_view, csv_attachment_view
from .. import get_title

request_logger = logging.getLogger('django.request')
logger = logging.getLogger(__name__)


@set_title(get_title('Homepage'))
@cache_control(public=True, s_maxage=3600, max_age=3600)
@html_view(template='djbp/examples/index.tpl')
def index(request):
    pass


@set_title(get_title('Form'))
@html_view(template='djbp/examples/form.tpl')
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

        example_error = forms.BooleanField(required=False)
        example_redirect = forms.BooleanField(required=False)

        example_hidden = forms.CharField(initial='I am hiding', widget=forms.HiddenInput)

        def clean(self):
            cleaned_data = super(MyForm, self).clean()
            if cleaned_data['example_bool']:
                raise forms.ValidationError('Tricked you! You do not really want to have example bool checked.')

            return cleaned_data

    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():

            if form.cleaned_data['example_error']:
                raise Exception('Ruh roh!')

            if form.cleaned_data['example_redirect']:
                messages.info(request, 'You have been redirected from a form hijax! How do you feel?')
                return HttpResponseRedirect(urlresolvers.reverse('messages_example'))

            messages.success(request, 'Form saved successfully')
            return HttpResponseRedirect(request.get_full_path())
        else:
            messages.error(request, 'Some required fields are missing or invalid. Details below.')
    else:
        form = MyForm()

    return {
        'form': form
    }


@set_title('Messages')
@html_view(template='djbp/examples/messages.tpl')
def messages_example(request):
    messages.set_level(request, messages.DEBUG)
    messages.debug(request, 'This is a debug message')
    messages.info(request, 'This is an informational message. It also happens to be a decently long one just to see how everything looks when it has to wrap to multiple lines')
    messages.success(request, '<strong>Great success!</strong> Whatever you did seems to have worked out!')
    messages.warning(request, 'Better watch out! This is a warning.')
    messages.error(request, 'Bad bad bad! Something really awful happened!')
    messages.add_message(request, 8000, 'Custom message level')
    pass


def redirect_internal(request):
    messages.success(request, 'You have been redirected successfully!')
    return HttpResponseRedirect(urlresolvers.reverse('messages_example'))


def redirect_external(request):
    return HttpResponseRedirect('https://github.com/kcolton/django-boilerplate')


@set_title(get_title('Foo'))
@cache_control(public=True, s_maxage=3600, max_age=3600)
@html_view(template='djbp/examples/foo.tpl')
def foo(request):
    pass


@set_title(get_title('Bar'))
@cache_control(public=True, s_maxage=3600, max_age=3600)
@html_view(template='djbp/examples/bar.tpl')
def bar(request):
    pass


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


def error(request):
    raise Exception('Oh no! Something went terribly wrong!')


@set_title(get_title('Log'))
@html_view(template='djbp/examples/log.tpl')
def log(request):
    request_logger.debug('request_logger debug message')
    request_logger.info('request_logger info message')
    request_logger.warning('request_logger warning message')
    request_logger.error('request_logger error message')
    request_logger.critical('request_logger critical message')

    logger.debug('module logger debug message')
    logger.info('module logger info message')
    logger.warning('module logger warning message')
    logger.error('module logger error message')
    logger.critical('module logger critical message')

    warnings.warn('this is about to be depricated. this warning should only be shown once', DeprecationWarning)

    # Trigger SQL to test SQL logging
    users = User.objects.all().count()

    return dict(manager=logging.Logger.manager)


@set_title(get_title('Info'))
@html_view(template='djbp/examples/info.tpl')
def info(request):
    pass


@set_title(get_title('Links'))
@html_view(template='djbap/examples/links.tpl')
def links(request):
    pass


