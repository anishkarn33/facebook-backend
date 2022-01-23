from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, UserProfile
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, UserProfileSerializer

# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @action(methods=['post'], detail=True)
    def change_password(self, request, *args, **kwargs):
        """
        API to change user's passwords
        """
        user_instance = self.get_object()
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        if user_instance.check_password(old_password) == True:
            user_instance.set_password(new_password)
            return Response(data='password changed sucessfully')
        else:
            return Response(data='wrong password')

    
    @action(methods=['get'], detail=False, permission_classes=[permissions.IsAuthenticated])
    def me(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)



class UserProfileViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]


