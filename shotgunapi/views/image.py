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
        # retrieve method handles the GET request that has an ID in url, a specific image
        # query a single image in the image table using the primary key
        image = Image.objects.get(pk=pk)
        # run through serializer to return response client side can read, currently python object
        serializer = ImageSerializer(image)
        #changed to json
        return Response(serializer.data)
        

    def list(self, request):
        # list method handles GET requests to get all the pets, returns JSON serialized list of pets
        # query all images
        image = Image.objects.all()
        # run through serializer to return response client side can read, currently python object
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)
    
    def create(self, request):  
        
    # create method handles POST request to add a row to image table/a new image object
    # query the scrapbook object , keys must match to client since data passed in being held in request.data dictionary
        scrapbook= Scrapbook.objects.get(pk=request.data["scrapbook"])
        image = Image.objects.create(
            image_url=request.data["image_url"],
            scrapbook = scrapbook
            
           
         )
        serializer = CreateImageSerializer(image)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
    # destroy method handles DELETE request to delete row in table 
    # query the pet by getting the pk and delete function
        scrapbook = Scrapbook.objects.get(pk=pk)
    # getting individual tag by primary key and deleting
        scrapbook.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
    
    # update method handles PUT request to update a row on image table 
        try:
            image = Image.objects.get(pk=pk)
           
            serializer = ImageSerializer(image, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Image.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    
    
class ImageSerializer(serializers.ModelSerializer):
   # this class determines how the Python data should be serialized to be sent back to client in JSON.
    class Meta:
    # Meta class holds configuration for serializer - saying use the Pet model and include the fields to serialize below.
        model = Image
        fields = ('id','image_url', 'scrapbook')
        depth = 2
    
        
class CreateImageSerializer(serializers.ModelSerializer):
   # this class determines how the Python data should be serialized to be sent back to client in JSON.
    class Meta:
     # Meta class holds configuration for serializer - saying use the Pet model and include the fields to serialize below.
        model = Image
        fields = ('id', 'image_url', 'scrapbook')
        depth = 2