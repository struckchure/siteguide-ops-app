from django.urls import path

from patients.views import (
	PatientCreateView,
	PatientUpdateView,
	PatientDeleteView,
	PatientListView
)

app_name = 'patients'

urlpatterns = [
	path('', PatientListView.as_view(), name='index'), # index
	path('patients/create/', PatientCreateView.as_view(), name='create'), # patient create view
	path('patients/<int:id>/update/', PatientUpdateView.as_view(), name='update'), # patient update view
	path('patients/<int:id>/delete/', PatientDeleteView.as_view(), name='delete'), # patient delete
	path('patients/', PatientListView.as_view(), name='list'), # patient list
]
