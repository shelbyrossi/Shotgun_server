"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from shotgunapi.models.scrapbook import Scrapbook
from shotgunapi.models.app_users import App_Users
from django.forms import ValidationError


class ScrapbookView(ViewSet):


    def retrieve(self, request, pk):   

        scrapbook = Scrapbook.objects.get(pk=pk)
        
        # getting individual scrapbook by pk
        # serializer converts object to send to client, JSON serialized
        # setting the value of serializer to the Scrapbook Serializer and passing your scrapbook object through
        serializer = ScrapbookSerializer(scrapbook)
        # returning a response of the serialized data
        return Response(serializer.data)

    def list(self, request):
       
        # handling get request for all scrapbook types and returning a 
        # response of JSON serialized list of scrapbook types 
        
        scrapbook = Scrapbook.objects.all()         
        userId = self.request.query_params.get('user_id', None)
        tagId =  self.request.query_params.get('tag_id', 0)
        
        if userId is not None:
            scrapbook = scrapbook.filter(user_id = userId)
            # if there is a userId, filter scrapbooks by userId 
        
        if int(tagId)!= 0: 
            # if there is a tagId, filter scrapbooks by tags
            # stepping into tags 
            scrapbook = scrapbook.filter(tags__id = tagId)
            
     
       
            
           
        # getting all() the tags
        serializer = ScrapbookSerializer(scrapbook, many=True)
        # passing through serializer and setting multiple (many=true)
        return Response(serializer.data)
        # returning a response of teh serialized data

    def destroy(self, request, pk):
        """Delete game"""
        scrapbook = Scrapbook.objects.get(pk=pk)
        # getting individual tag by primary key and deleting
        scrapbook.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        """Handle POST operations

        Returns
         Response -- JSON serialized scrapbook instances
         """
        #   creating a method for POSTING scrapbook

        user = App_Users.objects.get(user=request.auth.user)
        

        scrapbook = Scrapbook.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            state=request.data['state'],
            date=request.data['date'],
            destination=request.data['destination'],
            favorite_foodstop=request.data['favorite_foodstop'],
            soundtrack=request.data['soundtrack'],
            favorite_experience=request.data['favorite_experience'],
            other_info=request.data['other_info'],
            user=user

        )

        try:
            scrapbook.tags.set(request.data['tags'])
            serializer = ScrapbookSerializer(scrapbook)
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

        

    def update(self, request, pk=None):
        """Handle PUT requests for a scrapbook

        Returns:
            Response -- Empty body with 204 status code
        """
        user = App_Users.objects.get(user=request.auth.user)
       

        # Do mostly the same thing as Scrapbook, but instead of
        # creating a new instance of Scrapbook, get the Scrapbook record
        # from the database whose primary key is `pk`
        scrapbook = Scrapbook.objects.get(pk=pk)
        scrapbook.name = request.data["name"]
        scrapbook.description = request.data["description"]
        scrapbook.destination = request.data["destination"]
        scrapbook.state = request.data["state"]
        scrapbook.date = request.data["date"]
        scrapbook.favorite_foodstop = request.data["favorite_foodstop"]
        scrapbook.soundtrack = request.data["soundtrack"]
        scrapbook.favorite_experience = request.data["favorite_experience"]
        scrapbook.other_info = request.data["other_info"]
        scrapbook.user = user

        scrapbook.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class ScrapbookSerializer(serializers.ModelSerializer):
    """JSON serializer for tag types
    """
    # telling the serializer to use Tag model and include the fields
    class Meta:
        model = Scrapbook
        fields = ('id','name', 'description', 'state', 'date', 'destination',
                  'favorite_foodstop', 'soundtrack', 'favorite_experience', 'other_info', 'user', 'tags')
        depth = 3


class CreateScrapbookSerializer(serializers.ModelSerializer):
    """JSON serializer for tag types
    """
    class Meta:
        model = Scrapbook
        fields = ('id', 'name', 'description', 'state',  'date', 'destination',
                  'favorite_foodstop', 'soundtrack', 'favorite_experience', 'other_info', 'user', 'tags')
        depth = 2
