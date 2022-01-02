from .models import Newsfeed
from rest_framework import viewsets, permissions
from .seralizer import  NewsfeedSerializers

# Create your views here.


class NewsfeedViewset(viewsets.ModelViewSet):
    """
    API endpoint taht allows users to be viewed or edited.
    """
    queryset = Newsfeed.objects.all().order_by('-date_joined')
    serializer_class = NewsfeedSerializers
    permission_classes = [permissions.AllowAny]
