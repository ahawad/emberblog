from blog.models import Blog
from rest_framework import pagination
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        lookup_field = 'slug'
        fields = ('title','body','slug','post_create_date')
