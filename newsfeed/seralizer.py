from .models import Newsfeed
from rest_framework import serializers


class NewsfeedSerializers(serializers.ModelSerializer):
    class Meta:
        model = Newsfeed
        fields = ['body', 'date_created', 'date_updated']
