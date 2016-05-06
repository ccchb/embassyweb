from django.shortcuts import render

from django.forms.models import modelformset_factory

from models import Attendant

def signup(request):
    SignupFormSet = modelformset_factory(Attendant)
    done = False
    space_left = 70 - Attendant.objects.count()

    if request.method == 'POST':
        formset = SignupFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            done = True
    else:
        formset = SignupFormSet(queryset=Attendant.objects.none())

    return render(request, "geekend_signup.html", {
        "formset": formset,
        "done": done,
        "space_left": space_left,
    })
