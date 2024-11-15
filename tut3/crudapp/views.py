from django.shortcuts import render
from .models import DetailsModel
from .serializer import DetailsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def get_details(request):
    detailsobj=DetailsModel.objects.all()
    serializer=DetailsSerializer(detailsobj, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_details(request):
    serializer=DetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        detail = DetailsModel.objects.get(pk=pk)
    except detail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DetailsSerializer(detail)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DetailsSerializer(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

