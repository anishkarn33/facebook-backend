
from .models import Newsfeed
from rest_framework import  viewsets
from .seralizers import  NewsfeedSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import AnonymousUser
# Create your views here.


class NewsfeedViewset(viewsets.ModelViewSet):
    """
    API endpoint taht allows users to be viewed or edited.
    """
    queryset = Newsfeed.objects.all().order_by('-date_updated')
    serializer_class = NewsfeedSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if isinstance(self.request.user, AnonymousUser):
            return serializer.save()
        return serializer.save(user=self.request.user)