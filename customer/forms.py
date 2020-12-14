from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Create_user_form(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "User name"}))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={"placeholder": "Email"}))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Password"}))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


def clean_new_user_stock_form_data(request):
    if request.POST.get('threshold_low'):
        th_low = request.POST.get('threshold_low')
    else:
        th_low = None

    if (request.POST.get('threshold_high')):
        th_high = request.POST.get('threshold_high')
    else:
        th_high = None

    if request.POST.get('send_update'):
        send_update = True
    else:
        send_update = False

    error = None
    if th_high and th_low:
        if float(th_high) < float(th_low):
            error = '"Threshold high" should be greater than "Threshold Low"'

    cleaned_data = {'th_low': th_low,
                    'th_high': th_high,
                    'send_update': send_update,
                    'error': error,
                    }
    return cleaned_data
