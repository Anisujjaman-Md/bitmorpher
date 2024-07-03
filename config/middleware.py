from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from user.models import RequestLog, CustomUser

class RequestLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            RequestLog.objects.create(
                username=request.user.username,
                timestamp=datetime.now(),
                path=request.path
            )

class UserTypeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth_token = request.headers.get('Authentication-Token')
        if auth_token:
            try:
                user = CustomUser.objects.get(authentication_token=auth_token)
                request.user = user
            except CustomUser.DoesNotExist:
                request.user = None
