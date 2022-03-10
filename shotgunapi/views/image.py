"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from shotgunapi.models import Image
from shotgunapi.models import Scrapbook



class ImageView(ViewSet):
    """SHOTGUN IMAGE VIEW"""

    def retrieve(self, request, pk):
        """Handle GET requests for single image type

        Returns:
            Response -- JSON serialized image type
        """
        
        image = Image.objects.get(pk=pk)
        serializer = ImageSerializer(image)
        
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all app users

        Returns:
            Response -- JSON serialized list of app users
        """
        image = Image.objects.all()
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
         Response -- JSON serialized image instance
         """
       
        scrapbook= Scrapbook.objects.get(pk=request.data["scrapbook"])
        image = Image.objects.create(
            image_url=request.data["image_url"],
            scrapbook= scrapbook
            
           
         )
        serializer = CreateImageSerializer(image)
        return Response(serializer.data)
    
    
    
class ImageSerializer(serializers.ModelSerializer):
    """JSON serializer for app users
    """
    class Meta:
        model = Image
        fields = ('id','image_url', 'scrapbook')
        depth = 2
    
        
class CreateImageSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Image
        fields = ('id', 'image_url', 'scrapbook')
        depth = 2