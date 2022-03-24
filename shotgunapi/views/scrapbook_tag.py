"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from shotgunapi.models import Scrapbook_Tag



class ScrapbookTagView(ViewSet):
  
    # retrieve method handles the GET request that has an ID in url, a specific scrapbook
    def retrieve(self, request, pk):            
    # query a single scrapbook in the scrapbook table using the primary key
        scrapbook_tag = Scrapbook_Tag.objects.get(pk=pk)
    #run through serializer to return response client side can read, currently python object
        serializer = Scrapbook_TagSerializer(scrapbook_tag)
    #return response 
        return Response(serializer.data)
        

    def list(self, request):
     
     # list method handles GET requests to get all the pets, returns JSON serialized list of pets 
        scrapbook_tag = Scrapbook_Tag.objects.all()
                
        serializer = Scrapbook_TagSerializer(scrapbook_tag, many=True)
        return Response(serializer.data)
    
    
    def destroy(self, request, pk):
        """Delete game"""
        scrapbook_tag = Scrapbook_Tag.objects.get(pk=pk)
        # getting individual tag by primary key and deleting
        scrapbook_tag.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
class Scrapbook_TagSerializer(serializers.ModelSerializer):
    # this class determines how the Python data should be serialized to be sent back to client in JSON.
    class Meta:
        
    # Meta class holds configuration for serializer - saying use the Pet model and include the fields to serialize below.
        model = Scrapbook_Tag
        fields = ('id', 'tag', 'scrapbook')
        depth = 3