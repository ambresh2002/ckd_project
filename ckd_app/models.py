from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    serum_creatinine = models.FloatField()
    albumin = models.FloatField()
    rbc = models.FloatField()
    hemoglobin = models.FloatField()
    gfr = models.FloatField()
    ckd_prediction = models.CharField(max_length=10)  # Yes/No
    ckd_stage = models.IntegerField(null=True, blank=True)
    treatment_recommendation = models.TextField()

    def __str__(self):
        return f"{self.name} - Stage {self.ckd_stage if self.ckd_stage else 'No CKD'}"


