

# Create your views here.
import joblib
import numpy as np
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Patient # Import your model
import pandas as pd

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
 # Import your model

# Welcome Page
def welcome(request):
    return render(request, "welcome.html")

# Signup View
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created! Please log in.")
        return redirect('login')

    return render(request, "signup.html")

# Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('predict') # Redirect to prediction page
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')

    return render(request, "login.html")

# Logout View
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('welcome')

def all_patients(request):
    patients = Patient.objects.all()  # Fetch all records
    return render(request, "all_patients.html", {"patients": patients})


# Load trained models and scaler
rf_ckd_model = joblib.load("rf_ckd_model.pkl")
rf_stage_model = joblib.load("rf_stage_model.pkl")
scaler = joblib.load("scaler.pkl")

# Treatment guidelines
treatment_recommendations = {
    1: "Stage 1 CKD: You're in the early stage of CKD, which is great because you can still take control! Focus on eating a balanced diet, staying active, and keeping an eye on your blood pressure and blood sugar. Small lifestyle changes now can make a big difference in the long run!",
    2: "Stage 2 CKD: Your kidneys need a little extra care. Stay well-hydrated, cut down on salty foods, and be mindful of painkillers like NSAIDs—they can put extra strain on your kidneys. Regular check-ups will help you stay on track!",

    3: "Stage 3 CKD: Things are getting a bit more serious, but don’t worry—you've got this! Managing your blood pressure and diabetes is key, so follow your doctor's advice on medications. You might need to watch your protein intake too. A nephrologist (kidney specialist) can help guide you on the best next steps.",

    4: "Stage 4 CKD: At this stage, it's important to start planning ahead. Your doctor might talk to you about dialysis options, and adjusting your medications can help slow things down. Keep a close eye on any symptoms, and don’t hesitate to reach out for support.",
    5: "Stage 5 CKD: Your kidneys need the most support now, and dialysis or a kidney transplant might be necessary. It’s a tough road, but you’re not alone—your healthcare team will help you figure out the best path forward. Stay positive, and lean on your loved ones for support!"
}

@login_required(login_url='login')
def predict_ckd(request):
    if request.method == "POST":
        # Get user input from form
        name = request.POST.get("name")
        age = float(request.POST.get("age"))
        serum_creatinine = float(request.POST.get("serumCreatinine"))
        albumin = float(request.POST.get("albumin"))
        rbc = float(request.POST.get("rbc"))
        hemoglobin = float(request.POST.get("hemoglobin"))
        gfr = float(request.POST.get("gfr"))

        # Ensure input is a DataFrame with correct feature names
        input_features = pd.DataFrame([[gfr, albumin, rbc, hemoglobin, serum_creatinine]], 
                                      columns=["GFR", "Albumin", "RBC", "Hemoglobin", "Serum_Creatinine"])  # Match training feature names

        # Scale input using trained StandardScaler
        input_scaled = scaler.transform(input_features)

        # Predict CKD presence
        ckd_prediction = rf_ckd_model.predict(input_scaled)[0]

        if ckd_prediction == 0:
            ckd_stage = None
            treatment = "No CKD detected. Maintain a healthy lifestyle."
        else:
            # Predict CKD stage
            ckd_stage = rf_stage_model.predict(input_scaled)[0]
            treatment = treatment_recommendations.get(ckd_stage, "Consult a nephrologist.")

        # Save patient record
        patient = Patient.objects.create(
            name=name,
            age=age,
            serum_creatinine=serum_creatinine,
            albumin=albumin,
            rbc=rbc,
            hemoglobin=hemoglobin,
            gfr=gfr,
            ckd_prediction="Yes" if ckd_prediction == 1 else "No",
            ckd_stage=ckd_stage,
            treatment_recommendation=treatment
        )

        return render(request, "result.html", {
            "name": name,
            "ckd_prediction": ckd_prediction,
            "ckd_stage": ckd_stage,
            "treatment": treatment
        })

    return render(request, "predict.html")




from django.shortcuts import render
from .models import Patient  # Import your model




