from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Item, User
from .serializers import ItemSerializer, UserSerializer
from django.db.models import Q

@ensure_csrf_cookie
def serve_react_app(request):
    """Serve the React app for all frontend routes"""
    return render(request, 'index.html')

def home(request):
    return serve_react_app(request)

def add_data(request):
    return serve_react_app(request)

def choice(request):
    return serve_react_app(request)

def consoles_peripherals(request):
    return serve_react_app(request)

def create_console(request):
    return serve_react_app(request)

def database_display(request):
    return serve_react_app(request)

def database_signup(request):
    return serve_react_app(request)

def database_functionality(request):
    return serve_react_app(request)

def game_copies(request):
    return serve_react_app(request)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_route(request):
    return Response({
        'message': 'You have accessed a protected endpoint',
        'user_id': request.user.username
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_items(request):
    items = Item.objects.filter(user=request.user)
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def manage_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id, user=request.user)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_items(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    
    items = Item.objects.filter(user=request.user)
    
    if query:
        items = items.filter(
            Q(name__icontains=query) |
            Q(pubmanu__icontains=query)
        )
    
    if category:
        items = items.filter(category=category)
        
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
