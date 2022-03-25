from django.urls import path
from customer import views


urlpatterns = [

    path("home",views.CustomerIndex.as_view(),name="custhome"),
    path("accounts/register",views.SignUp.as_view(),name="signup"),
    path("accounts/login", views.SignIn.as_view(), name="signin"),
    path("accounts/logout",views.Signout ,name="signout"),
    path("accounts/password/reset", views.PasswordReset.as_view(), name="passwordreset"),

]