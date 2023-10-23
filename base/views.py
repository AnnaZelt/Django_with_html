from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index(req):
    data = {'name':'bla', 'age': 11}
    return Response(data)

@api_view(['GET'])
def about(req):
    return Response('about')

@api_view(['GET'])
def bla1(req):
    return Response('bla1')

@api_view(['GET'])
def bla2(req):
    return Response('bla2')

@api_view(['GET'])
def bla3(req):
    return Response('bla3')
