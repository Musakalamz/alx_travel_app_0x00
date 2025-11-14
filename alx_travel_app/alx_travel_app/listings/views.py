from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='get',
    operation_description="Welcome endpoint for ALX Travel App API"
)
@api_view(['GET'])
def welcome_view(request):
    """Welcome endpoint for the ALX Travel App API"""
    return Response({
        "message": "Welcome to ALX Travel App API",
        "status": "success"
    })