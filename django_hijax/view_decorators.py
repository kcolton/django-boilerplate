import functools


def set_title(title):
    def decorator(view_func):
        @functools.wraps(view_func)
        def wrapper(request, *args, **kwargs):
            request.title = title
            response = view_func(request, *args, **kwargs) or dict()
            response['X-Title'] = title
            return response
        return wrapper
    return decorator