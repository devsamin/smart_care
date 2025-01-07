from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime
# Create your models here.

APPOINTMENT_STATUS = [
    ('Completed', 'Completed'),
    ('Padding', 'Padding'),
    ('Running', 'Running')
]
APPOINMENT_TYPE = [
    ('Offline', 'Offline'),
    ('Online', 'Online'),
]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_type = models.CharField(choices=APPOINMENT_TYPE, max_length=20)
    appointment_status = models.CharField(choices=APPOINTMENT_STATUS, max_length=20, default="Padding")
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Patient : {self.patient.user.first_name} - Doctor : {self.doctor.user.first_name}"