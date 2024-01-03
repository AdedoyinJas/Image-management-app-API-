# from django_filters.rest_framework import FilterSet
# from .models import Image
# import django_filters


# class ImageFilter(FilterSet):
#   emotion = django_filters.CharFilter(method='filter_by_emotion')
  
#   def filter_by_emotion(self, queryset, name , value):
#     return queryset.fiilter(emotion__iexact=value)
#   class Meta:
#     model = Image
#     fields = ['emotion']

# class ImageFilter(django_filters.FilterSet):
#     emotion = django_filters.CharFilter(method='filter_by_emotion')

#     def filter_by_emotion(self, queryset, name , value):
#       return queryset.fiilter(emotion__iexact=value)
#     class Meta:
#       model = Image
#       fields = ['emotion']