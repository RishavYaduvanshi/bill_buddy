from functools import wraps
import jwt
from django.http import HttpResponseForbidden


def jwt_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        secret_key = "THIS IS A TEST SECRET KEY AND IS USED FOR TESTING!"
        info, *_ = args
        request = info.context.get("request")
        if request:
            token = request.META.get("HTTP_AUTHORIZATION")
        if token:
            token = token.replace("Bearer ", "")
            try:
                payload = jwt.decode(token, secret_key, algorithms=["HS256"])
                return view_func(request, *args, **kwargs)
            except jwt.ExpiredSignatureError:
                return HttpResponseForbidden("Token has expired")
            except jwt.DecodeError:
                return HttpResponseForbidden("Invalid token")
        else:
            return HttpResponseForbidden("Token is missing")

    return _wrapped_view
