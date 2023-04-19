import django_filters
from .models import *



class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = usersPosts
        fields = '__all__'