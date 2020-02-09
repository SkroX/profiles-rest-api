from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test api view."""

    def get(self,request,format=None):
        """Retrurns a list of api view"""

        apiview=["avsv","sfasa"]

        return Response({"message":"Hello","apiview":apiview})
