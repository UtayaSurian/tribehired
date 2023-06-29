from django.http import HttpResponseForbidden

class RestrictAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            return HttpResponseForbidden("No Access! This is just an assessment.")
        return self.get_response(request)
