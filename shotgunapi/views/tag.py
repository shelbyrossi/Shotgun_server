"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from shotgunapi.models.tag import Tag



class TagView(ViewSet):
  

    def retrieve(self, request, pk):
    # retrieve method handles GET request that has ID in url, a specific tag

        tag = Tag.objects.get(pk=pk)
        # getting individual tag by pk
        # serializer converts object to send to client
        # setting the value of serializer to the Tag Serializer and passing your tag object through
        serializer = TagSerializer(tag)
        # returning a response of the serialized data
        return Response(serializer.data)


    def list(self, request):
    # list method handles GET request to get all the tags   
        tag = Tag.objects.all()
        # getting all() the tags
        serializer = TagSerializer(tag, many=True)
        # passing through serializer and setting multiple (many=true)
        return Response(serializer.data)
        # returning a response of the serialized data 

    def destroy(self, request, pk):
        """Delete game"""
        tag = Tag.objects.get(pk=pk)
        # getting individual tag by primary key and deleting 
        tag.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request):
        
        #   creating a method for POSTING tags 
        tag = Tag.objects.create(
            label=request.data["label"],
           
         )
        serializer = CreateTagSerializer(tag)
        return Response(serializer.data)
    
    def update(self, request, pk):
      
        try:
            tag = Tag.objects.get(pk=pk)
           
            serializer = CreateTagSerializer(tag, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)



class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for tag types
    """
    # telling the serializer to use Tag model and include the fields 
    class Meta:
        model = Tag
        fields = ('id','label')
        depth = 1
        
class CreateTagSerializer(serializers.ModelSerializer):
    """JSON serializer for tag types
    """
    class Meta:
        model = Tag
        fields = ('id','label')
        depth = 1