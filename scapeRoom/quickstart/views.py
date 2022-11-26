from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from scapeRoom.quickstart.serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
def book_a_ticket(request):
    print(request.data)
    return Response({'name':'mehdi'})

def ticket(request):
    print(request.data)
    return Response({'name':'mehdi'})

