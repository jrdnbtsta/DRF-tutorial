from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    endpoint that allows individual users to be viewed / edited
    """

    queryset = User.objects.all().order_by('-datejoined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    endoint that allows groups to be viewed or edited
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

