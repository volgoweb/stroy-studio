# -*- coding: utf-8 -*-
from django import forms
from .models import CallMeClaim

class CallMeClaimForm(forms.ModelForm):
    class Meta():
        model = CallMeClaim
