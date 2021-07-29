from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View


class PatientCreateView(View):

	template_name = 'patients/patient-create.html'

	def get(self, request):
		return render(request, self.template_name)


class PatientUpdateView(View):
	
	template_name = 'patients/patient-update.html'

	def get(self, request):
		return render(request, self.template_name)



class PatientDeleteView(View):
	
	def get(self, request, id):
		patient = get_object_or_404(Patient, id=id)
		patient.delete()

		return redirect('patients:index')


class PatientListView(View):

	template_name = 'patients/patient-list.html'

	def get(self, request):
		return render(request, self.template_name)
