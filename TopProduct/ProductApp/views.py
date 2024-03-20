from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import USerData,Companies,Categories

from .Serializers import(CompaniesSerializer,CategoriesSerializer,UserInputSerializer)


class RetriveOperationView(APIView):

    def post(self,request , *args,**kwargs):
        serializer= UserInputSerializer(data=request.data)
        if serializer.is_valid():
            top = serializer.validated_data['top']
            

