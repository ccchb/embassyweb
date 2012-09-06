from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import HttpResponseForbidden
from django.utils import timezone
from django.conf import settings
from models import DoorState

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

