from views import getCurrentDoorState

def getDoorState():
	state = getCurrentDoorState()
	if state:
		return state.isOpen
	else:
		return None

def roomstatus(request):
	res = {
		"door": getDoorState(),
	}
	return {"roomstatus": res}

