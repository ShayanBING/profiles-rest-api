from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""
    def get(self,request,format=None):
         """Return list of ApiView Features"""
         an_apiview=[
         'Use Http method as function(get,post,patch,put,delete) ',
         'is similar to traditional Django View',
         'gives you the most control over your application logic',
         'its map to url'
         ]

         return Response({'message':"Hello!","an_apiview":an_apiview})
