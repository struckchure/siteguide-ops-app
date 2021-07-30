from django import forms
from django.utils.translation import gettext_lazy as _

from patients.models import Patient
from patients.utils import DateInput


class PatientForm(forms.ModelForm):

    started_meds_on = forms.DateField(required=False, widget=DateInput)

    class Meta:
        model = Patient
        exclude = [
            'date',
            'updated'
        ]
        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'gender': _('Gender'),
            'age': _('Age'),
            'doctor_name': _('Doctor'),
            'doctor_fees': _('Doctor Fees'),
            'started_meds_on': _('Started Meds On')
        }
        help_texts = {
            'started_meds_on': _('When you started taking you meds (if any)')
        }
        widgets = {
            'gender': forms.Select(attrs={
                'class': 'appearance-none',
                'placeholder': 'Select your gender'
            }),
            'doctor_fees': forms.NumberInput(attrs={
                'value': '500'
            })
        }
