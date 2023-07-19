from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView, Response
# Create your views here.


class HomeView(APIView):
    def get(self, request):
        return Response('hi')
