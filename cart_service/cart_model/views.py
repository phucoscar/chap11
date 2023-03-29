from django.shortcuts import render
from cart_model.models import Cart
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
import json

@csrf_exempt
def addToCart(request):
    req = json.loads(request.body)
    uname = req['Username']
    product_id = req['ProductId']
    quantity = req['Quantity']
    resp = {}
    cart = Cart()
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

        cart.fname = val1['First Name']
        cart.lname = val1['Last Name']
        cart.email = uname

        # get product info
        url = 'http://127.0.0.1:3001/get-one-product/'
        d2 = {}
        d2["ProductId"] = product_id
        data = json.dumps(d2)
        headers = {'Content-Type': 'application/json'}
        response =  requests.post(url, data=data, headers=headers)
        val2 = json.loads(response.content.decode('utf-8'))
        val2 = val2['data']

        cart.product_id = product_id
        cart.product_name = val2['product_name']

        cart.quantity = quantity
        

        # save comment into database
        cart.save()

        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = cart.to_json()

    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All field is mandatory'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')


@csrf_exempt
def getCartByUsername(request):
    req = json.loads(request.body)
    uname = req['Username']
    data = Cart.objects.all().filter(email=uname)
    cartData = []
    for value in data.values():
        cartData.append(value)
    resp = {}
    if cartData:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = cartData
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '404'
        resp['message'] = "Cart is empty"
    return HttpResponse(json.dumps(resp), content_type = 'application/json')