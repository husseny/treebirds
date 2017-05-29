# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from models import Comment
import json, sys

# Create your views here.

def demo(request):
	return render(request, 'nestedcomments/demo.html', {})

def add_comment(request):
	post_data = json.loads(request.body)
	try:
		comment = post_data['comment']
	except (KeyError):
		return HttpResponse(-1)
	#result = Comment.add_comment(comment)
	#result = Comment.add_nested_comment(5, comment)
	#result = Comment.delete_comment(1)
	return HttpResponse(result)

def get_comments(request):
	result = Comment.view_comments()
	return JsonResponse(json.dumps(result), safe=False)