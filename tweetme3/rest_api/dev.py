from django.contrib.auth import get_user_model
from rest_framework import authentication

User = get_user_model()

class Devauthentication(authentication.BasicAuthentication):
    def authenticate(self, request):
        qs = User.objects.filter(id=2)
        user = qs.order_by("?").first() # ? means radom users
        return (user, None)
