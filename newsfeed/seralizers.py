from rest_framework.fields import CurrentUserDefault
from rest_framework.utils.field_mapping import ClassLookupDict
from .models import Newsfeed
from rest_framework import serializers


class NewsfeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsfeed
        fields = ['id', 'body', 'date_created', 'date_updated', 'user']
        read_only_fields = ['id',]
