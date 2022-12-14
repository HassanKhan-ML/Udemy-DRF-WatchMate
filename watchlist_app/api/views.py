import imp
import re
from xmlrpc.client import ResponseError
from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse
from watchlist_app.api.serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.



# Function Basec View
@api_view(['GET', 'POST']) 
def movie_list(request):
  if request.method == 'GET':
    movies = Movie.objects.all()
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    serializer = MovieSerializers(data= request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)

@api_view(['GET','PUT', 'PATCH', 'DELETE' ])
def movie_details(request, pk):
  
  if request.method == 'GET':
    movie =Movie.objects.get(pk= pk)
    serializer = MovieSerializers(movie)
    return Response(serializer.data)
  
  if request.method == 'PUT':
    movie = Movie.objects.get(pk= pk)
    serializer = MovieSerializers(movie, data= request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
    
  # if request.method == 'PATCH':
    
  if request.method == 'DELETE':
    movie = Movie.objects.get(pk= pk)
    movie.delete()
    return Response()