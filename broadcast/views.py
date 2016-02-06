from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.views import generic
from django.utils import timezone
from .models import Group, TwitterKeys
from .models import Token
from random import randint
import json
import twitter
from twitter import TwitterError
import requests
import argparse
import os
import sys


#REQUEST STUFF
URL = 'https://api.groupme.com/v3'

#HELPER FUNCTIONS
def get(response):
	return response.json()['response']

#VIEW CLASSES
class IndexView(generic.ListView):
	template_name = 'broadcast/index.html'
	context_object_name = 'groups'
	def get_queryset(self):
		return Group.objects.all()

class GroupMeHomeView(generic.ListView):
	context_object_name = 'groups'
	template_name = 'broadcast/groupme_home.html'
	def get_queryset(self):
		return Group.objects.all()

class TwitterHomeView(generic.ListView):
	context_object_name = 'twitter'
	template_name = 'broadcast/twitter_home.html'
	def get_queryset(self):
		return TwitterKeys.objects.first()

#VIEW FUNCTIONS
def addTwitter(request):
	#Get a TwitterKeys object with posted information, change its username, and save it to database
	key = TwitterKeys(consumer_key=request.POST['consumer_key'], consumer_secret=request.POST['consumer_secret'], access_token_key=request.POST['access_token_key'], access_token_secret=request.POST['access_token_secret'])
	api = twitter.Api(consumer_key=key.consumer_key,
	                      consumer_secret=key.consumer_secret,
	                      access_token_key=key.access_token_key,
	                      access_token_secret=key.access_token_secret)
	try:
		api.VerifyCredentials()
	except TwitterError as e:
		return HttpResponseRedirect(reverse('broadcast:twitter_home'))
	key.screen_name = json.loads(str(api.VerifyCredentials()))['screen_name']
	key.save()
	return HttpResponseRedirect(reverse('broadcast:twitter_home'))

def saveTwitter(request):
	#save the active state of the TwitterKeys objects
	key = TwitterKeys.objects.first()
	key.active = request.POST.get('active', False)
	key.save()
	return HttpResponseRedirect(reverse('broadcast:twitter_home'))

def removeTwitter(request):
	#remove the TwitterKeys object
	keys = TwitterKeys.objects.all()
	for key in keys:
		key.delete()
	return HttpResponseRedirect(reverse('broadcast:twitter_home'))

def sendMessage(request):
	#groupme side
	msgText = request.POST['message']
	#make random string for guid
	guid = str(randint(-32000,32000))
	token = Token.objects.first()
	msgData = json.dumps({"message":{"source_guid":guid, "text": msgText}})
	print "Sending message " + msgText
	for g in Group.objects.all():
		if g.active:
			print requests.post("https://api.groupme.com/v3/groups/" + g.group_id + "/messages?token=" + token.token_text, data=msgData, headers={'Content-Type': 'application/json'})
	#twitter side
	keys = TwitterKeys.objects.all()
	for key in keys:
		if key.active:
			api = twitter.Api(consumer_key=key.consumer_key,
		                      consumer_secret=key.consumer_secret,
		                      access_token_key=key.access_token_key,
		                      access_token_secret=key.access_token_secret)
			api.PostUpdate(msgText)
	return HttpResponseRedirect(reverse('broadcast:index'))

def wipeGroups(request):
	#remove API token from database
	tokens = Token.objects.all()
	for t in tokens:
		t.delete()
	#remove groups associated with API token from database
	for g in Group.objects.all():
		g.delete()
	return HttpResponseRedirect(reverse('broadcast:groupme_home'))

def saveGroups(request):
	#save active state for all groups
	checklist = request.POST.getlist('active')
	for g in Group.objects.all():
		g.active = (g.group_id in checklist)
		g.save()
	return HttpResponseRedirect(reverse('broadcast:groupme_home'))

def addGroupMeApi(request):
	#change the API token for the new groups to be used for messaging service
	token = request.POST['groupmeApiToken']
	tokenToAdd = Token(token_text=token)
	tokenToAdd.save()
	groups = get(requests.get(URL + '/groups' + '?token=' + token, params={'per_page' : 100}))
	if not groups:
		return HttpResponseRedirect(reverse('broadcast:groupme_home'))
	for g in groups:
		groupToAdd = Group(group_name=g['name'], group_id=g['group_id'])
		groupToAdd.save()
	return HttpResponseRedirect(reverse('broadcast:groupme_home'))