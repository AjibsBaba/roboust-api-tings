from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import AccountsSerializer


class AccountsViewset(viewsets.ViewSet):
    """
    An account viewset for listing and retrieving users
    """

    def list(self, request):
        queryset = User.objects.all()
        serializer = AccountsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AccountsSerializer(user)
        return Response(serializer.data)
