from rest_framework import serializers
from .models import Link,Advocate,Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name','logo','summary','advocates']


class CompanyMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name']


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = ['name','url']


class AdvocateSerializer(serializers.ModelSerializer):
    link = LinkSerializer(source='links',many=True)
    company = CompanyMiniSerializer(read_only=True)
    class Meta:
        model = Advocate
        fields = ['id','name','username','profile_pic','short_bio','long_bio','advocate_since','company','link']
