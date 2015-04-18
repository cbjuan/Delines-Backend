from models import *
from rest_framework.serializers import ModelSerializer

class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
    def create(self, validated_data):
        # Create the book instance
        position = Position(latitude=validated_data['latitude'], longitude=validated_data['longitude'],
                            elevation=validated_data['elevation'])
        position.save()

        return position

class RouteSerializer(ModelSerializer):
    class Meta:
        model = Route
    position = PositionSerializer(read_only=False, required=False, many=True)

    def create(self, validated_data):
        route = Route(transport=validated_data['transport'])
        route.save()
        for item in validated_data['position']:
            try:
                position = Position(latitude=item['latitude'], longitude=item['longitude'],
                                    elevation=item['elevation'])
            except:
                position = Position(latitude=item['latitude'], longitude=item['longitude'])
            position.save()
            route.position.add(position)
            route.save()
        user = User.objects.get(id=1)
        user.routes.add(route)
        user.save()
        return route

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
    routes = RouteSerializer(read_only=False, required=False, many=True)
    def create(self, validated_data):
        user = User()
        user.save()
        for item in validated_data['route']:
            route = Route(transport=item['transport'])
            route.save()
            '''
            for item in validated_data['position']:
                position = Position(latitude=item['latitude'], longitude=item['longitude'],
                                    elevation=item['elevation'])
                position.save()
                route.position.add(position)
                route.save()
            '''
        return route
    def update(self, instance, validated_data):
        instance.routes.add(validated_data['route'])
        instance.save()