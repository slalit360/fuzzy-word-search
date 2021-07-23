from django.conf.urls import url
from django.urls import path
from .views import index_view, search, getJson, get_index

urlpatterns = [
    path('', index_view , name = 'index_view'),
    path('search/', search, name = 'search'),
    path('getJson/', getJson, name='matched_words_json'),
    path('hello/', get_index, name='hello'),
]
