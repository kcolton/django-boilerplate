from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from lib.django.views.decorators import HtmlView
from django.views.decorators.cache import cache_control


@cache_control(public=True, s_maxage=3600, max_age=3600)
@HtmlView(template='example/index.tpl')
def index(request):
    return {}


@HtmlView(template='example/form.tpl')
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

        example_required_bool = forms.BooleanField()
        example_bool = forms.BooleanField(required=False)
        example_char = forms.CharField(help_text="This is some text to help you. <a href=\"http://google.com\">Need more help</a>")
        example_choice = forms.ChoiceField(choices=CHOICES)
        example_date = forms.DateField()
        example_datetime = forms.DateTimeField(help_text="Some tip for this date field")
        example_decimal = forms.DecimalField()
        example_email = forms.EmailField()
        example_file = forms.FileField()
        example_float = forms.FloatField()
        example_image = forms.ImageField()
        example_integer = forms.IntegerField()
        example_multi = forms.MultipleChoiceField(choices=CHOICES)

    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Form saved successfully')
            return HttpResponseRedirect(request.get_full_path())
    else:
        form = MyForm()

    return {
        'form': form
    }

@cache_control(public=True, s_maxage=3600, max_age=3600)
@HtmlView(template='example/foo.tpl')
def foo(request):
    return {}


@cache_control(public=True, s_maxage=3600, max_age=3600)
@HtmlView(template='example/bar.tpl')
def bar(request):
    return {}


