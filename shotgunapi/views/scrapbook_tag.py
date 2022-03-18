"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from shotgunapi.models import Scrapbook_Tag



class ScrapbookTagView(ViewSet):
    """SHOT GUN SCRAPBOOK TAG view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single scrapbooktag

        Returns:
            Response -- JSON serialized game type
        """
        
        scrapbook_tag = Scrapbook_Tag.objects.get(pk=pk)
        serializer = Scrapbook_TagSerializer(scrapbook_tag)
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all scrapbook tags

        Returns:
            Response -- JSON serialized list of all scrapbook tags
        """
        scrapbook_tag = Scrapbook_Tag.objects.all()
        tagId =  self.request.query_params.get('tag_id', None)
        
        if tagId is not None:
            scrapbook_tag = scrapbook_tag.filter(tag_id = tagId)
            
        serializer = Scrapbook_TagSerializer(scrapbook_tag, many=True)
        return Response(serializer.data)
    
    
    def destroy(self, request, pk):
        """Delete game"""
        scrapbook_tag = Scrapbook_Tag.objects.get(pk=pk)
        # getting individual tag by primary key and deleting
        scrapbook_tag.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class Scrapbook_TagSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Scrapbook_Tag
        fields = ('id', 'tag', 'scrapbook')
        depth = 3