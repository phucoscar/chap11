from django.shortcuts import render
from book_model.models import Book
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import requests
import json


@csrf_exempt
def createBook(request):
    image = request.FILES.get('image')
    id = request.POST.get('id')
    name = request.POST.get('name')
    author = request.POST.get('author')
    availability = request.POST.get('availability')
    description = request.POST.get('description')
    price = request.POST.get('price')

    resp = {}
    if image and id and name and author and availability and description and price:
        # call image_service to store image into db
        data = {}
        data["ProductId"] = id
        url = 'http://127.0.0.1:5005/upload-product-img/'
        files ={'image': image}
        response =  requests.post(url, data=data, files=files)
        rs = json.loads(response.content.decode('utf-8'))
        print(response)
        book = Book()
        book.id = id
        book.name = name
        book.author = author
        book.availability = availability
        book.description = description
        book.price = price
        res = book.to_json()
        res['image_path'] = rs['path']
        resp['status'] = "Success"
        resp['status_code'] = '200'
        resp['data'] = res
    else:
        resp['status'] = "Failed"
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

# @csrf_exempt
# def getBookById(request):
#     req = json.loads(request.body)
#     book_id = req['product_id']
#     bookdata = Book.objects.all().filter(id=book_id)
#     data = []
#     for value in bookdata.values():
#         data.append(value)