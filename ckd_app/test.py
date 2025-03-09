from django.test import TestCase
from .models import Patient

class PatientModelTest(TestCase):
    def test_create_patient(self):
        """Test if a patient record is created successfully"""
        patient = Patient.objects.create(
            name="Test Patient",
            age=40,
            serum_creatinine=1.2,
            albumin=4.5,
            rbc=5.0,
            hemoglobin=14.0,
            gfr=90,
            ckd_prediction="No",
            ckd_stage=None,
            treatment_recommendation="Maintain a healthy lifestyle"
        )
        self.assertEqual(patient.name, "Test Patient")
        self.assertEqual(patient.age, 40)
