from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json
from .fuzzy import  getMatchingWord


def get_index(request):
    if request.method == 'GET':
        return JsonResponse({'msg': 'Hello'})
    else:
        return JsonResponse({'msg': 'Post request is handled'})

def index_view(request):
    """
    index page view
    :param request:
    :return: renders index.html
    """
    return render(request, 'index.html')


def search(request):
    """
    Autocomplete ajax call
    :param request:
    :return: HttpResponse which consist list of words
    """
    word_count = {}
    if request.is_ajax():
        word_searched = request.GET.get('term').strip().lower()
        matchedWords  = getMatchingWord(word_searched)
        data = json.dumps(matchedWords)
    else:
        data = ''
    return HttpResponse(data, 'application/json')

def getJson(request):
    """
    prepares list of matching words as per criteria

    :param request:
    :return: JsonResponse
    """
    if request.method == 'GET':
        word_searched = request.GET.get('term').strip().lower()
        matchedWords = getMatchingWord(word_searched)
        if len(matchedWords) == 0:
            return JsonResponse({'Matched_Word': "Word not found."})
        else:
            return JsonResponse({'Matched_Word': matchedWords})
    else:
        return JsonResponse({'Matched_Word': "Request Not found!"})


