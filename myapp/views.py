from django.shortcuts import render
from django.http.response import HttpResponse
from urllib import parse
#import chardet
import requests
import json
from bs4 import BeautifulSoup
import urllib.request, json
from django.http import HttpResponse

# Create your views here.
def index_template(request):
    name = request.GET.get('name')
    area = request.GET.get('area')
    print(area)
    if name == None:
        chihoulist = []
        with urllib.request.urlopen("https://hellojsonfile.netlify.app/updated2.json") as url:
            data = json.loads(url.read())
            for i in data['universities']:
                if i['area'] == area:
                    course = i['jap_name']

                    chihoulist.append(i['jap_name'])

        myapp_data2 = dict()
        myapp_data2["list"] = chihoulist
        return render(request, 'index.html',{'myapp_data2':myapp_data2})
    elif area == None:
        session = requests.Session()
        course = name + " 進路"
        url = session.get(f'https://www.google.co.jp/search?q={course}').text

        # グーグルへ接続
        soup = BeautifulSoup(url,'html.parser')
        f = soup.select('div.kCrYT > a ')[0]['href'].replace('/url?q=', '').split('&sa')[0]
        f2 = soup.select('div.kCrYT > a > h3.zBAuLc')[0].text

        myapp_data = dict()
        myapp_data["new"] = f
        myapp_data["newtitle"] = f2
        return render(request, 'index.html', {'myapp_data': myapp_data})

