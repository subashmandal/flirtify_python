from flirtify.serialization import Serializationclass, UserDataSerializer, UpdateDataSerializer
from flirtify.models import UserData


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist

import requests
# from .models import TableOne

@api_view(['POST', 'GET'])

def showUserData(request):
    try:
        if request.method == 'POST':
            results = UserData.objects.all()
            serialize = Serializationclass(results,many = True)
            return Response({
                "status": True,
                "data": serialize.data
                }, status=status.HTTP_200_OK)
        elif request.method == 'GET':
            return Response({
                "status" : False,
                "message" : "Please Send Post request"
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except ObjectDoesNotExist:
        return Response({
            "error": "UserData not found"
            }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST', 'GET'])  
def filterData(request):
    if request.method != 'POST':
        return Response({
            "Status" : False,
            "Message" : "Please Send Post request to fetch user data."
        }, status= 405)
    try:
        # Extract data from POST request
        email = request.data.get('email', None)
        name = request.data.get('name', None)
        user_id = request.data.get('id', None)

        # Create a filter dictionary
        filters = {}
        if email:
            filters['email'] = email
        if name:
            filters['name'] = name
        if user_id:
            filters['id'] = user_id

        # Query the database with the filters
        results = UserData.objects.filter(**filters)

        # Serialize the results
        serialize = Serializationclass(results, many=True)

        # Return the JSON response with status
        return Response({"status": True, "data": serialize.data})

    except Exception as e:
        # Handle any errors and return an appropriate response
        return Response({"status": False, "error": str(e)}, status=400)

@api_view(['POST'])
def addUserData(request):
    if request.method == "POST":
        try:
            serialize = UserDataSerializer(data = request.data)
            if serialize.is_valid():
                serialize.save()
                return Response({
                    "status": True,
                    "message" : "Data inserted Successfully",
                    "data" : serialize.data
                }, status = status.HTTP_201_CREATED)
            else:
                return Response({
                    "status": False,
                    "message": "Failed to insert data.",
                    "error" : serialize.errors,
                }, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "status": False,
                "error": str(e),
            }, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({
            "status": False,
            "message": "Invalid request Method",
        })

@api_view(['PUT'])
def updateUserData(request):
    email = request.data.get('email')

    if not email:
        return Response({
            "status" : False,
            "error": "Email is required to update user data",
        }, status= status.HTTP_400_BAD_REQUEST)
    
    # Fetch the user object by email
    users = UserData.objects.filter(email=email)
    if not users.exists():
        return Response({
            "status": False,
            "error": "User with the provided email does not exist."
        }, status=status.HTTP_404_NOT_FOUND)
    
    # Loop through each user and update the data
    updated_users = []
    for user in users:
        serializer = UpdateDataSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            updated_users.append(serializer.data)
        else:
            return Response({
                "status": False,
                "error": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        "status": True,
        "data": updated_users
    }, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def deleteUserData(request):
    email = request.data.get('email')

    if not email:
        return Response({
            "status": False,
            "error": "Email is required to delete user data."
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Fetch the user(s) with the provided email
        users = UserData.objects.filter(email=email)

        if not users.exists():
            return Response({
                "status": False,
                "error": "No user found with the provided email."
            }, status=status.HTTP_404_NOT_FOUND)

        # Delete the user(s)
        deleted_count, _ = users.delete()

        return Response({
            "status": True,
            "message": f"Successfully deleted {deleted_count} user(s) with email {email}."
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "status": False,
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def displaydata(request):
    try:
        response = requests.get('http://127.0.0.1:8000/show')
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()  # Assuming the API returns JSON data
        else:
            data = []  # In case of an error, we can set data to an empty list
    
        # Pass the data to the template
            return render(request, 'home.html', {'data': data})
    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        return render(request, 'home.html', {'data': [], 'error': str(e)})