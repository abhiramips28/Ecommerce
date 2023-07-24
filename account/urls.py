from django.urls import path

from .views import Register, VerifyUser, MyTokenObtainPairView

urlpatterns = [
    path('register',Register.as_view(),name='register'),
    path('verifyuser/', VerifyUser.as_view()),
    path('login/', MyTokenObtainPairView.as_view()),

]