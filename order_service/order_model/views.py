from django.shortcuts import render
from order_model.models import Order
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
import json

@csrf_exempt
def create_order(request):
    req = json.loads(request.body)
    uname = req['Username']
    product_id = req['ProductId']
    quantity = req['Quantity']
    resp = {}
    order = Order()
    if uname and product_id and quantity:
        # get info user
        url = 'http://127.0.0.1:8000/userinfo/'
        d1 = {}
        d1["User Name"] = uname
        data = json.dumps(d1)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=data, headers=headers)
        val1 = json.loads(response.content.decode('utf-8'))
        val1 = val1['data']

        order.fname = val1['First Name']
        order.lname = val1['Last Name']
        order.email = uname

        # get product info
        url = 'http://127.0.0.1:3001/get-one-product/'
        d2 = {}
        d2["ProductId"] = product_id
        data = json.dumps(d2)
        headers = {'Content-Type': 'application/json'}
        response =  requests.post(url, data=data, headers=headers)
        val2 = json.loads(response.content.decode('utf-8'))
        val2 = val2['data']

        order.product_id = product_id
        order.product_name = val2['product_name']

        order.quantity = quantity
        order.total_price = int(quantity) * int(val2['price'])
        order.status = 'Pending'

        # save comment into database
        order.save()

        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = order.to_json()

    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All field is mandatory'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')