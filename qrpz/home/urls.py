from django.urls import path
from . import views
urlpatterns = [
   
    
    path('post/',views.scanner,name="scanner"),
    path('',views.home,name="home"),
    path('puzzle',views.puzzle,name="puzzle"),
]
