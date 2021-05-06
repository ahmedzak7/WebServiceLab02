from django.shortcuts import render, redirect, HttpResponse
import requests
from django.http import JsonResponse
import json
import xmltodict
from bs4 import BeautifulSoup
from .models import Product
# Create your views here.


def index(request):
    response = requests.get('https://api.flyallover.com/api/sitemap/sitemap.xml/support')
    decoded_response = response.content.decode('utf-8')
    response_json = json.loads(json.dumps(xmltodict.parse(decoded_response)))
    location_urls = response_json['urlset']['url']
    context = {
        'locations': location_urls
    }
    return render(request, "rest/index.html", context)


def getProducts(request):
    pass
    products = Product.objects.all()
    response = """<?xml version="1.0"?>

                   <soap:Envelope
                   xmlns:soap="http://www.w3.org/2003/05/soap-envelope/"
                   soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">

                   <soap:Body>
                     <m:GetPostsResponse>
                """

    for product in products:
        response += "<m:ProductDetails>" + "<m:ProductName>" + product.name + "</m:ProductName>" + "<m:ProductDescription>" + product.description + "</m:ProductDescription>" + "<m:ProductPrice>" + str(product.price) + "</m:ProductPrice>" + "</m:ProductDetails>" + "\n"

    response += """   </m:GetPostsResponse>
                    </soap:Body>
                   </soap:Envelope> """
    soup = BeautifulSoup(response, "xml") 
    print(soup)
    return HttpResponse(soup, content_type='text/xml')