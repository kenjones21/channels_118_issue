from django.shortcuts import render
from channels.handler import AsgiRequest

# Create your views here.
def subscribe(request):

    raise AsgiRequest.ResponseLater()