# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from product_model.models import product_details
import requests

@csrf_exempt
def get_product_data(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    prodata = product_details.objects.all()
    for tbl_value in prodata.values():
        data.append(tbl_value)
        # If data is available then it returns the data.
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@csrf_exempt
def get_product_by_Id(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    productId = json.loads(request.body)
    prodata = product_details.objects.all().filter(product_id=productId['ProductId'])

    for tbl_value in prodata.values():
        data.append(tbl_value)
        # If data is available then it returns the data.

    # call book_service
    if len(data) == 0:
        url = 'http://localhost:5006/get-book/'
        d = {}
        d['product_id'] = productId['ProductId']
        d=json.dumps(d)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=url, data=d, headers=headers)
        res = json.loads(response.content.decode('utf-8'))
        res = res['data']
        if res:
            res = res[0]
            res['product_id'] = res.pop("id")
            res['product_name'] = res.pop("name")
            data.append(res)
    
      # call clothe_service
    if len(data) == 0:
        url = 'http://localhost:5007/get-clothe/'
        d = {}
        d['product_id'] = productId['ProductId']
        d=json.dumps(d)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=url, data=d, headers=headers)
        res = json.loads(response.content.decode('utf-8'))
        res = res['data']
        if res:
            res = res[0]
            res['product_id'] = res.pop("id")
            res['product_name'] = res.pop("name")
            data.append(res)
    
      # call electronic_service
    if len(data) == 0:
        url = 'http://localhost:5009/get-electronic/'
        d = {}
        d['product_id'] = productId['ProductId']
        d=json.dumps(d)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=url, data=d, headers=headers)
        res = json.loads(response.content.decode('utf-8'))
        res = res['data']
        if res:
            res = res[0]
            res['product_id'] = res.pop("id")
            res['product_name'] = res.pop("name")
            data.append(res)

      # call shoe_service
    if len(data) == 0:
        url = 'http://localhost:5008/get-shoe/'
        d = {}
        d['product_id'] = productId['ProductId']
        d=json.dumps(d)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=url, data=d, headers=headers)
        res = json.loads(response.content.decode('utf-8'))
        res = res['data']
        if res:
            res = res[0]
            res['product_id'] = res.pop("id")
            res['product_name'] = res.pop("name")
            data.append(res)

    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data[0]
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')