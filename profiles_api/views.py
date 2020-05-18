from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializer


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


