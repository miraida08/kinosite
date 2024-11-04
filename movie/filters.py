from django_filters import FilterSet
from .models import Movie
class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'actor': ['exact'],
            'director': ['exact'],
            'janre': ['exact'],
            'status_movie': ['exact'],
            'country': ['exact'],
            'year': ['gt', 'lt'],



        }
