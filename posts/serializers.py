from rest_framework import serializers
from .models import Post


class FileSerializer(serializers.ModelSerializer):

	class Meta():
		model = Post
		fields = ('title','video','content','publish_date','timestamp','updated')



