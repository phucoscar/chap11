from django.shortcuts import render
from image_model.models import Image
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import requests
import json
import os

@csrf_exempt
def updateProductImage(request):
    file = request.FILES.get('image')
    product_id = request.POST.get('ProductId')
    if file and product_id :
        # Tao duong dan
        image_dir = os.path.join('D:\KientrucVathietkephanmem', 'images')
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)

        # path toi file
        image_path = os.path.join(image_dir, file.name)

        # Ghi file vao o dia
        with open(image_path, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)

        image = Image()
        image.product_id = product_id
        image.path = image_path
        image.save()
        return JsonResponse({
            "status": 'Success',
            "status_code": '200',
            "path": image_path
        })
    else:
        return JsonResponse({"status": "Failed"})
