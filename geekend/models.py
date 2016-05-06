# -*- coding: utf-8 -*-

from django.db import models
from django.forms import ModelForm

class Attendant(models.Model):
    handle = models.CharField(max_length=32,
        verbose_name="Pseudonym")
    vegetarian = models.BooleanField(
        verbose_name="Vegetarier")
    needs_place_to_sleep = models.BooleanField(
        verbose_name="Benötige Schlafplatz")
    email = models.CharField(max_length=128, blank=True,
        verbose_name="Schlafplatz-Rückmeldung an diese eMail-Adresse")
    comments = models.TextField(blank=True,
        verbose_name="Kommentar")

class SignupForm(ModelForm):
    class Meta:
        model = Attendant

