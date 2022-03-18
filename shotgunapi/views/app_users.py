"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from shotgunapi.models import App_Users
from rest_framework.decorators import action



class AppUserView(ViewSet):
    """SHOTGUN APP USERS VIEW"""

    def retrieve(self, request, pk):
        """Handle GET requests for single app user type

        Returns:
            Response -- JSON serialized app user type
        """
        
        app_user = App_Users.objects.get(pk=pk)
        serializer = App_UsersSerializer(app_user)
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all app users

        Returns:
            Response -- JSON serialized list of app users
        """
        app_user = App_Users.objects.all()
        serializer = App_UsersSerializer(app_user, many=True)
        return Response(serializer.data)
    
    
    @action(methods=['get'], detail=False)
    def currentuser(self, request):
        user = App_Users.objects.get(user=request.auth.user)
        serializer = App_UsersSerializer(user)
        return Response(serializer.data)
       
    
class App_UsersSerializer(serializers.ModelSerializer):
    """JSON serializer for app users
    """
    class Meta:
        model = App_Users
        fields = "__all__"
        depth = 1
        
        