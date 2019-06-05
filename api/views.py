from django.shortcuts import render, redirect
import requests
from django.http.response import JsonResponse
BASE_URL = 'https://api.odsay.com/v1/api/searchPubTransPath'
API_KEY = '/Z+FNNIFCh0VTSfz+wgotg'


def send_get(request):
    query = make_url(request, API_KEY)

    print(BASE_URL+query)
    res = requests.get(BASE_URL+query)
    print(res)
    if (res.status_code == 200):
        result = res.json()
        print(result)
        return JsonResponse(result)
    else:
        return JsonResponse({'message': 'severError', 'code': res.status_code})


def make_url(request, api_key):
    keyword = request.GET
    query = '?'
    for key, value in keyword.items():
        query += '{}={}&'.format(key, value)
    query += 'apiKey={}'.format(api_key)
    return query