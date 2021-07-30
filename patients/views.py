from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.forms.models import model_to_dict

from patients.models import Patient
from patients.forms import PatientForm


class PatientCreateView(View):

    template_name = 'patients/patient-create.html'

    def get(self, request):
        patient_form = PatientForm()
        context = {
            'patient_form': patient_form,
            'patients': self.get_queryset()
        }

        return render(request, self.template_name, context)

    def post(self, request):
        patient_form = PatientForm(request.POST)
        context = {
            'patient_form': patient_form,
            'patients': self.get_queryset()
        }

        if patient_form.is_valid():
            patient_form.save()

            return redirect('patients:create')

        patient_form = PatientForm()

        return render(request, self.template_name, context)

    def get_queryset(self):
        return Patient.objects.order_by('-updated')


class PatientUpdateView(View):

    template_name = 'patients/patient-update.html'

    def get(self, request, id):
        patient = get_object_or_404(Patient, id=id)
        patient_update_form = PatientForm(
            instance=patient,
            initial=model_to_dict(patient)
        )

        context = {
            'patient': patient,
            'patient_form': patient_update_form
        }

        return render(request, self.template_name, context)

    def post(self, request, id):
        patient = get_object_or_404(Patient, id=id)
        patient_update_form = PatientForm(
            request.POST,
            instance=patient,
            initial=model_to_dict(patient)
        )

        if patient_update_form.is_valid():
            patient_update_form.save()

            return redirect('patient:list')

        context = {
            'patient': patient,
            'patient_form': patient_update_form
        }

        return render(request, self.template_name, context)


class PatientDeleteView(View):

    def get(self, request, id):
        patient = get_object_or_404(Patient, id=id)
        patient.delete()

        return redirect('patients:list')


class PatientListView(View):

    template_name = 'patients/patient-list.html'

    def get(self, request):
        context = {
            'patients': self.get_queryset()
        }

        return render(request, self.template_name, context)

    def get_queryset(self):
        return Patient.objects.order_by('-updated')
