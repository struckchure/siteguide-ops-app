from django.db import models


class Patient(models.Model):

    class GENDER(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    gender = models.CharField(max_length=10, choices=GENDER.choices, blank=True)
    age = models.PositiveIntegerField(blank=False)
    disease = models.TextField()
    doctor_name = models.CharField(max_length=255)
    doctor_fees = models.PositiveIntegerField(default=500)
    started_meds_on = models.DateField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_gender(self):
        if self.gender == 'M':
            return 'Male'
        elif self.gender == 'F':
            return 'Female'
        else:
            return 'N/A'
