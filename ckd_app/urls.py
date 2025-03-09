from django.urls import path
from .views import predict_ckd, all_patients, welcome, signup, user_login, user_logout

urlpatterns = [
    path("", welcome, name="welcome"),  # Welcome page
    path("signup/", signup, name="signup"),  # Signup page
    path("login/", user_login, name="login"),  # Login page
    path("logout/", user_logout, name="logout"),  # Logout page
    path("predict/", predict_ckd, name="predict"),  # CKD prediction page
    path("patients/", all_patients, name="all_patients"),  # Patient records
]

