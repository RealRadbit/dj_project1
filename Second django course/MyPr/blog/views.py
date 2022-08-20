from xml.dom.pulldom import SAX2DOM
from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')