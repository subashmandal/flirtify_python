from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import random
import requests

def home(request):
    response = requests.post('http://127.0.0.1:8000/show')
    data = response.json()

    # Extract status and data from the response
    status = data.get("status", False)
    user_data = data.get("data", [])

    if status and user_data:
        randomData = random.choice(user_data)
        user_id = randomData.get('id')
    request1 = {
        "id": user_id,
    }
    responce1 = requests.post('http://127.0.0.1:8000/filterdata', data = request1)
    data1 = responce1.json()

    status1 = data1.get("status", True)
    user_data1 = data1.get("data", [])


# Create your views here.
    context = {
        'status': status,
        'data': user_data,
        "status1" : status1,
        'data1': user_data1
    }
    
    return render(request, 'home.html', context)

def profile(request):
    return render(request, 'profile.html')

def fetch_user_data(request):
    if request.method == 'POST':
        responce = requests.post('http://127.0.0.1:8000/show')
        data1 = responce.json()

        status = data1.get("status", True)
        user_data1 = data1.get("data", [])

        if status and user_data1:
            return JsonResponse(data1)
        else:
            return JsonResponse({"status" : False, "message" : "Failed to fetch data from database."})
    else:
        return JsonResponse({"status" : False, "message" : "Invalid request method."})
    
def insertUser(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        