from django.utils.timezone import now
from accounts.models import CustomUser
from accounts.backends import JWTAuthentication
from rest_framework import authentication


class SetLastVisitMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = authentication.get_authorization_header(request).decode('utf-8')
        if auth_header:
            user = JWTAuthentication().authenticate(request)
            if user:
                # Update last visit time after request finished processing.
                CustomUser.objects.filter(pk=user[0].pk).update(last_visit=now())
        return self.get_response(request)