from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.utils import timezone
from django.conf import settings
from models import DoorState
import json
import time

def getCurrentDoorState(now=None):
	try:
		lastState = DoorState.objects.order_by('-start')[0]
	except IndexError:
		return None

	if not now:
		now = timezone.now()

	if now - lastState.end > settings.DOORSTATE_TIMEOUT:
		return None

	return lastState

@csrf_exempt
@require_POST
def setDoorState(request):
	if request.POST.get("secret") != settings.DOORSTATE_SECRET:
		return HttpResponseForbidden("wrong or missing secret")

	try:
		isOpen = {"0": False, "1": True}[request.POST.get("isopen")]
	except KeyError:
		return HttpResponseBadRequest("isopen must be 0 or 1")

	now = timezone.now()
	lastState = getCurrentDoorState(now)
	if lastState:
		lastState.end = now
		lastState.save()

	if not lastState or lastState.isOpen != isOpen:
		newState = DoorState()
		newState.start = now
		newState.end = now
		newState.isOpen = isOpen
		newState.save()

	# build response
	if isOpen:
		res = r"""
----------------------------------

         +------+
         |      |\
         |      | \
         | \o/  |  |
         |  M   |  |
         | / \  |  |
---------+======+  |--------------
                 \ |
                  \|
"""
	else:
		res = r"""
----------------------------------

         +------+
         |      |
         |      |
         |*~    |
         |      |
         |      |
---------+======+-----------------
"""

	return HttpResponse(res, "text/plain")

def spaceapi(request):
	"""Implements the HackerSpace Status API

	See https://hackerspaces.nl/spaceapi/ for details."""

	site = 'http://%s%%s' % Site.objects.get_current().domain

	# check door state
	isOpen = False
	status = 'Sensor is broken'
	lastchange = 0
	currentDoorstate = getCurrentDoorState()
	if currentDoorstate:
		isOpen = currentDoorstate.isOpen
		status = {
			True: 'Open for public',
			False: 'Closed',
			}[isOpen]
		lastchange = time.mktime(currentDoorstate.start)

	data = {
		'api': '0.12',
		'space': 'Embassy of Nerdistan',
		'logo': site % '/static/Embassy.png',
		'icon': {
			'open': site % '/static/icon-open.png',
			'closed': site % '/static/icon-closed.png'},
		'url': site % reverse('embassyweb.views.index'),
		'open': isOpen,
		'status': status,
		'lastchange': lastchange,

		'address': 'Embassy of Nerdistan, AUCOOP Bremen e.V., '\
				'Weberstrasze 18, 28203 Bremen, Germany',
		'lat': 53.07208,
		'lon': 8.82183,
		'contact': {
			'twitter': '@embassyof',
			'email': 'vorstand..ccchb.de',
			'ml': 'ccc..lists.erleuchtet.org',
		},
		'feeds': [
			{
				'name': 'blog',
				'type': 'application/rss+xml',
				'url': site % reverse('feed-rss')},
			{
				'name': 'blog',
				'type': 'application/atom+xml',
				'url': site % reverse('feed-atom')},
			{
				'name': 'calendar',
				'type': 'text/calendar',
				'url': 'http://ccchb.de/CCCHB-Kalender.ics'},
		],
	}
	response = HttpResponse(json.dumps(data, ensure_ascii=False),
			mimetype='application/json')
	response['Access-Control-Allow-Origin'] = '*'
	response['Cache-Control'] = 'no-cache'
	return response

