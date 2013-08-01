from lib.django.views.decorators import JsonView
from django.views.decorators.cache import never_cache

@never_cache
@JsonView()
def load(request):
    output = {
        'is_authenticated': request.user.is_authenticated()
    }

    if (request.user.is_authenticated()):
        output['id'] = request.user.id
        output['email'] = request.user.email

    return output

    