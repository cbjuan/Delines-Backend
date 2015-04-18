from django.shortcuts import render

# Create your views here.

# views.py
from models import *
from serializers import *
from rest_framework.viewsets import ModelViewSet
#from rest_framework_jsonp.renderers import JSONPRenderer
from django.http import HttpResponse

class UserViewSet(ModelViewSet):
    #renderer_classes = (JSONPRenderer,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RouteViewSet(ModelViewSet):
    #renderer_classes = (JSONPRenderer,)
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class PositionViewSet(ModelViewSet):
    #renderer_classes = (JSONPRenderer,)
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


def PopulateData(request):

    position1 = Position(latitude=40.957784, longitude=-5.6667782, elevation=15)#Facultad Ciencias
    position1.save()
    position2 = Position(latitude=40.96152, longitude=-5.668691, elevation=17) #Colegio Fray Luis de Leon
    position2.save()
    position3 = Position(latitude=40.96152, longitude=-5.668691, elevation=15) #Colecio Fonseca
    position3.save()

    route = Route()
    route.save()
    route.position.add(position1)
    route.position.add(position2)
    route.position.add(position3)
    route.save()

    user = User()
    user.save()
    user.routes.add(route)
    user.save()

    return HttpResponse("Populating database... Correct!")
