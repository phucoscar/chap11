from django.shortcuts import render
from electronic_model.models import Electronic
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import requests
import json


@csrf_exempt
def createElectronic(request):
    image = request.FILES.get('image')
    id = request.POST.get('id')
    name = request.POST.get('name')
    brand = request.POST.get('brand')
    availability = request.POST.get('availability')
    description = request.POST.get('description')
    price = request.POST.get('price')

    resp = {}
    if image and id and name and brand and availability and description and price:
        # call image_service to store image into db
        data = {}
        data["ProductId"] = id
        url = 'http://127.0.0.1:5005/upload-product-img/'
        files ={'image': image}
        response =  requests.post(url, data=data, files=files)
        rs = json.loads(response.content.decode('utf-8'))
        print(response)
        electronic = Electronic()
        electronic.id = id
        electronic.name = name
        electronic.brand = brand
        electronic.availability = availability
        electronic.description = description
        electronic.price = price
        electronic.save()
        
        res = electronic.to_json()
        res['image_path'] = rs['path']
        resp['status'] = "Success"
        resp['status_code'] = '200'
        resp['data'] = res
    else:
        resp['status'] = "Failed"
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@csrf_exempt
def getElectronicById(request):
    req = json.loads(request.body)
    electronic_id = req['product_id']
    elecData = Electronic.objects.all().filter(id=electronic_id)
    data = []
    for value in elecData.values():
        data.append(value)
    resp = {}
    resp['data'] = data
    return HttpResponse(json.dumps(resp), content_type = 'application/json')