from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from oauth2_provider.decorators import rw_protected_resource
from .signals import login_signal

import requests

from .serializers import CreateUserSerializer, ReadUserSerializer

CLIENT_ID = 'rRBpv8fC85SzyUqc1Rrl2KFEu8BocdCPmZQnOrrG'
CLIENT_SECRET = 'DYWwosnMri4decbX63xr9MxO9LV3iA7V9qPFiIgpRO4Uvleygr0nOF7JZDpN9Y69i3y1Za7shCXxKLnjlJCCa4CmChpaQqNPiSRYxRh2vejt90McIKgC94qgAiI0OTHm'


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """"
    Registers user to the server. Input should be in the format:
    {"email": "email@domain.com", "password": "password"}
    """
    # Put the data from the request into the serializer
    serializer = CreateUserSerializer(data=request.data)
    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save()
        success = {
            'message': f"Successfully registered user: [{request.data['email']}]"
        }
        return Response(success)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    """
    Gets tokens with username and password. Input should be in the format:
    {"email": "email@domain.com", "password": "password"}
    """
    r = requests.post(
        'http://127.0.0.1:8000/o/token/',
        data={
            'grant_type': 'password',
            'username': request.data['email'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    if r.status_code == requests.codes.ok:
        login_signal.send(token, email=request.data['email'])
    return Response(r.json(), status=r.status_code)


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    """"
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    """
    r = requests.post(
        'http://127.0.0.1:8000/o/token/',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    if r.status_code == requests.codes.ok:
        login_signal.send(refresh_token, email=request.data['email'])
    return Response(r.json(), status=r.status_code)


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    """
    Method to revoke tokens.
    {"token": "<token>"}
    """
    r = requests.post(
        'http://127.0.0.1:8000/o/revoke_token/',
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return success message (would be empty otherwise)
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@rw_protected_resource()
def session_details(request):
    """
    Method to get user details
    """
    serializer = ReadUserSerializer(request.user)
    return Response(serializer.data)
