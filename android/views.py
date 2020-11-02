from django.shortcuts import render
from .models import Talk
from .serializers import talkSerializer
import json
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .analysis import analysis


@api_view(['GET', 'POST'])
def talkViewSet(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        result = analysis(data['back'])
        return JsonResponse(result)