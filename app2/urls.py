from django.urls import path
from . import views
 
 urlpatterns = [
     path("" , views.index , name="index"),
     path("brian" , views.brain, name="brain"),
     path("david", voews.david, name="david")

 ]