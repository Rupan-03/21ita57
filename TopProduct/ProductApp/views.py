from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

from .models import USerData,Companies,Categories

from .Serializers import(CompaniesSerializer,CategoriesSerializer,UserInputSerializer)


class RetriveOperationView(APIView):

    def post(self,request , *args,**kwargs):
        serializer= UserInputSerializer(data=request.data)
        if serializer.is_valid():
            top = serializer.validated_data['top']
            minPrice = serializer.validated_data['minPrice']
            maxPrice = serializer.validated_data['maxPrice']
            
            auth_data = {
                'companyName': 'goMart',
                'clientID': 'e66299e4-d3ba-4140-a017-8e1ac7089dd4',
                'clientSecret': 'CctTKJTXKvCUELrA',
                'ownerName': 'Thangarupan',
                'ownerEmail': 'danialrupan2018@gmail.com',
                'rollNo': '721221205057'
            }

        try:
            
            auth_response = requests.post('http://20.244.56.144/products/auth', json=auth_data)

           
            if auth_response.status_code == 201:

                auth_response_data = auth_response.json()

                access_token = auth_response_data.get('access_token')

                return Response({'access_token': access_token}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        product_response = requests.get()

