from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers

from rest_framework import status

# Create your views here.

class HelloApiView(APIView):
    """Test api view."""

    serialzer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Retrurns a list of api view"""

        apiview=["avsv","sfasa"]

        return Response({"message":"Hello","apiview":apiview})


    def post(self,request):
        """creates a hello message with name"""

        serializer=serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get("name")
            message="hello {0}".format(name)

            return Response({'message':message})

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({"message":"put"})

    def patch(self,request,pk=None):
        return Response({"message":"patch"})

    def delete(self,request,pk=None):
        return Response({"message":"delete"})
