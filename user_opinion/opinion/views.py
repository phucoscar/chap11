from django.shortcuts import render
from opinion.models import Opinion as uopinion
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
import json

@csrf_exempt
def create_comment(request):
    req = json.loads(request.body)
    uname = req['Username']
    product_id = req['ProductId']
    content = req['Content']
    resp = {}
    opinion = uopinion()
    if content:
        # get info user
        url = 'http://127.0.0.1:8000/userinfo/'
        d1 = {}
        d1["User Name"] = uname
        data = json.dumps(d1)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=data, headers=headers)
        val1 = json.loads(response.content.decode('utf-8'))
        val1 = val1['data']

        opinion.fname = val1['First Name']
        opinion.lname = val1['Last Name']
        opinion.email = uname

        # get product info
        url = 'http://127.0.0.1:3001/get-one-product/'
        d2 = {}
        d2["ProductId"] = product_id
        data = json.dumps(d2)
        headers = {'Content-Type': 'application/json'}
        response =  requests.post(url, data=data, headers=headers)
        val2 = json.loads(response.content.decode('utf-8'))
        val2 = val2['data']

        opinion.product_id = product_id
        opinion.product_name = val2['product_name']

        # set contend comment
        opinion.content = content

        # save comment into database
        opinion.save()

        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = opinion.to_json()

    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Content field is mandatory'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@csrf_exempt
def getAllCommentByProductId(request):
    req = json.loads(request.body)
    product_id = req['ProductId']
    resp = {}
    comments = uopinion.objects.all().filter(product_id=product_id)
    data = []
    for comment in comments.values():
        data.append(comment)
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '404'
        resp['message'] = "Not found any comment"
    return HttpResponse(json.dumps(resp), content_type = 'application/json')
 
