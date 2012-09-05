from django.utils import timezone
from django.conf import settings
from models import DoorState

def getDoorState():
	try:
		lastState = DoorState.objects.order_by('-end')[0]
	except IndexError:
		return None

	if timezone.now() - lastState.end > settings.DOORSTATE_TIMEOUT:
		return None

	return lastState.state

def roomstatus(request):
	res = {
		"door": getDoorState(),
	}
	return {"roomstatus": res}

