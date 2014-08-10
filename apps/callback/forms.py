# -*- coding: utf-8 -*-
from django import forms
from .models import Callback
from captcha.fields import CaptchaField

class CallbackForm(forms.ModelForm):
    captcha = CaptchaField(
        label = '',
        help_text = u'Введите код с картинки',
    )
    class Meta():
        model = Callback

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', {})
        super(CallbackForm, self).__init__(*args, **kwargs)

    def clean(self):
        values = super(CallbackForm, self).clean()
        if getattr(self.request, 'user'):
            current_user = User.objects.get(pk = self.request.user.pk)
            values['author_user'] = current_user
        # TODO получить и записать IP
        return values
