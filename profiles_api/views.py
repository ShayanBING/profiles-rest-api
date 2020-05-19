from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializer
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializer.HelloSerializer

    def get(self,request,format=None):
         """Return list of ApiView Features"""
         an_apiview=[
         'Use Http method as function(get,post,patch,put,delete) ',
         'is similar to traditional Django View',
         'gives you the most control over your application logic',
         'its map to url'
         ]

         return Response({'message':"Hello!","an_apiview":an_apiview})

    def post(self,request):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        #if serializer value is valid do our logic
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message':message})
        else:
            # error http 400 bad request
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        """handle updating object"""
        #pk is used for id for the object that you want to be update
        # put is update a row
        serializer = self.serializer_class(data=request.data)
        name = 'shayan'
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message':name})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None):
        """update partial of and object"""
        # patch is update a field
        return Response({'message':'PATCH'})

    def delete(self,request,pk=None):
        """delete a object"""
        return Response({'message':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """test api view set"""
    serializer_class = serializer.HelloSerializer
    def list(self,request):
        """return hello message"""
        a_viewset=[
            'uses action (list,retrive,create,update,partial_update,destroy)',
            'automaticly maps to urls using routers',
            'provide more functionality with less code',
            'work with database and models'
        ]

        return Response({'meesage':'list','a_viewset':a_viewset})
    def create(self,request):
        """create hello message"""
        serializer = self.serializer_class (data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """handle geting an object by its id"""
        return Response({'http_method':'get'})
    def update(self,request,pk=None):
        """hande update object by its id"""
        return Response({'http_method':'put'})
    def partial_update(self,request,pk=None):
        """hande partial update object by its id"""
        return Response({'http_method':'patch'})
    def destroy(self,request,pk=None):
        """hande delete object by its id"""
        return Response({'http_method':'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profile"""
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email')

class UserLoginApiView(ObtainAuthToken):
    """handle create user authnectication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES





