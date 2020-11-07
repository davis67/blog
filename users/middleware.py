from .import models


class AddProfilePicture(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        self.process_request(request)
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        self.process_response(request, response)
        # the view is called.

        return response

    def process_request(self, request):
        print(request)
        return None

    def process_response(self, request, response):
        print(request)
        # Process the response
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('----- Middleware view %s' % view_func.__name__)
        print(view_func)
        return None
