from rest_framework import serializers

from ps2api.models import Raspberry


class RaspberrySerializer(serializers.ModelSerializer):

    user = serializers.RelatedField(source='PS2User', read_only=True)
    longitude = serializers.FloatField(max_value=180, min_value=-180)
    latitute = serializers.FloatField(max_value=90, min_value=-90)
    parkspots = serializers.IntegerField()
    created = serializers.DateTimeField()

    class Meta:
        model = Raspberry
        fields = ('url', 'id', 'user', 'longitude', 'altitude', 'parkspots' 'created')

    class Meta:
        model = Raspberry
        fields = ('url', 'id', 'created', 'name', 'user')
        extra_kwargs = {
            'url': {
                'view_name': 'ps2api:raspberry-detail',
            }
        }

    def create(self, validated_data):
        return Raspberry(**validated_data)

    def update(self, instance, validated_data):
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.latitute = validated_data.get('latitute', instance.latitute)
        instance.parkspots = validated_data.get('parkspots', instance.parkspots)
        return instance
