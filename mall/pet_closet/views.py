from django.shortcuts import render

# Create your views here.
import os
import time

from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from pet_closet.models import PetCloset
from user.models import UserProfile

import json
import time
import requests
import re
from fake_useragent import UserAgent



@csrf_exempt
def add_view(request):
    if request.method=="POST":
        cloth_name = request.POST.get('cloth_name')
        avatar = request.FILES.get('avatar')
        season = request.POST.get('season')
        style = request.POST.get('style')
        function = request.POST.get('function')
        remark = request.POST.get('remark')
        # user = request.myuser
        user_profile = request.POST.get('cloth_name')
        print(user_profile)
        try:
            # user = UserProfile.objects.create(username='bzx', email='1333', phone='13131',
            #                       password='1313', nickname='bzx1')
            pet_closet = PetCloset.objects.create(cloth_name=cloth_name, avatar=avatar, season=season,
                                                  style=style, function=function, remark=remark,
                                                  user_profile_id='bzx')
        except Exception as e:
            print(e)
            result = {'code': 10103, 'error': '用户名已经存在'}
            return JsonResponse(result)
        result = {"code": 200, "msg": "上传照片成功"}
        return JsonResponse(result)




class Weather:
    # ---------根据主机IP获取定位-----
    def search_region_by_ip(self,computer_ip):
        url = 'https://www.ip138.com/iplookup.asp?ip=%s&action=2' % computer_ip
        headers = {'User-Agent': UserAgent().random}
        try:
            html = requests.get(url=url, headers=headers).content.decode('gb2312')
            print(html)
            region = re.findall('ip_result = {"ASN归属地":".*?[省市](.*?)市[\W|\w]', html, re.S)
            return region
        except Exception:
            return JsonResponse({'code': 50001,'error':'查询region失败'})

    def search_weather(self,region):
        url = "http://wthrcdn.etouch.cn/weather_mini?city=%s" % region
        try:
            # response = requests.get(url,timeout=8)
            response = requests.get(url)
            weather_data = json.loads(response.text)
            # print(weather_data)
            date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            year = str(date).split("-")[0]
            month = str(date).split("-")[1]
            day = weather_data['data']['forecast'][0]['date']
            city = weather_data['data']['city']
            weather_high = weather_data['data']['forecast'][0]['high']
            weather_low = weather_data['data']['forecast'][0]['low']
            a = weather_low.split(" ")[1]
            # print(a)
            print(year,month, day, weather_high, weather_low)
            region_weather=(year+'/'+month+'/'+day+'  '+weather_high+'  '+weather_low)
            return region_weather
        except:
            return JsonResponse({'code': 50001,'error':'查询weather失败'})


def weather_view(request, bzx):
    url = 'http://ip.42.pl/raw'
    computer_ip= requests.get(url).text
    print(computer_ip)
    weather=Weather()
    # region = weather.search_region_by_ip(computer_ip)[0]
    # print(region)
    region = '北京'
    region_weather=weather.search_weather(region)
    # result = {'code':200,}
    # result = {'code': 200, 'data': {'info': '123'}}
    # return JsonResponse(result)
    return JsonResponse({'code': 200,'data': {'region':region,'weather': region_weather}})


def list_view(request):
    if request.method=='GET':
        all_clothes=PetCloset.objects.all().order_by('-created_time')
        count = len(all_clothes)
        clothes_json = []
        for i in all_clothes:
            clothes_json2 = {}
            clothes_json2['id'] = i.id
            clothes_json2['cloth_name'] = i.cloth_name
            # clothes_json2['avatar'] = i.avatar
            clothes_json2['season'] = i.season
            clothes_json2['style'] = i.style
            clothes_json2['function'] = i.function
            clothes_json2['remark'] = i.remark
            clothes_json2['created_time'] = i.created_time
            clothes_json2['updated_time'] = i.updated_time
            clothes_json.append(clothes_json2)
        return JsonResponse({"code": 200, "obj": clothes_json})
    elif request.method == "GET":
        clothes_json = []
        json_str = request.body
        json_obj = json.loads(json_str)
        cloth_name = json_obj['name']
        all_notice = PetCloset.objects.filter(title=cloth_name)
        if all_notice:
            clothes_json2 = {}
            clothes_json2['id'] = all_notice.id
            clothes_json2['cloth_name'] = all_notice.cloth_name
            # clothes_json2['avatar'] = all_notice.avatar
            clothes_json2['season'] = all_notice.season
            clothes_json2['style'] = all_notice.style
            clothes_json2['function'] = all_notice.function
            clothes_json2['remark'] = all_notice.remark
            clothes_json2['created_time'] = all_notice.created_time
            clothes_json2['updated_time'] = all_notice.updated_time
            clothes_json.append(clothes_json2)
            print(clothes_json)
            return JsonResponse({"code": 200, "obj":clothes_json})

        else:
            return JsonResponse({"code": 300})

# from urllib import response

# -------根据地区得到天气---------


#
#
# url = 'http://ip.42.pl/raw'
# computer_ip= requests.get(url).text
# print(computer_ip)
# computer_ip='125.123.68.154'
# computer_ip='101.39.225.103'
# computer_ip='101.39.225.128'
# region=search_region_by_ip(computer_ip)[0]
# search_weather(region)
# search_weather('北京')
#
