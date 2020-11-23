import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def home_view(request, *args, **Kwargs):
    return render(request, "pages/feed.html")


def tweet_list_view(request, *args, **Kwargs):
    return render(request, "tweets/list.html")

def tweet_detail_view(request, tweet_id, *args, **Kwargs):
    return render(request, "tweets/detail.html", context={"tweet_id": tweet_id}) 

def tweet_profile_view(request, username, *args, **Kwargs):
    return render(request, "tweets/profile.html", context={"profile_username": username})    

