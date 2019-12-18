from django.shortcuts import render
import requests

def index(request):
    return render(request, 'base.html')

def apitest(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'apitest.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })