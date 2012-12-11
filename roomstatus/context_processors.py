from views import getCurrentDoorState, getCurrentLeaseState

def getDoorState():
	state = getCurrentDoorState()
	if state:
		return state.isOpen
	else:
		return None

def getLeaseState():
	state = getCurrentLeaseState()
	if state:
		return state.leases
	else:
		return None

def roomstatus(request):
	res = {
		"door": getDoorState(),
		"leases": getLeases(),
	}
	return {"roomstatus": res}

