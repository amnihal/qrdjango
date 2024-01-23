from django.urls import path
from . import views
urlpatterns = [
   
    
    path('post/',views.scan,name="scan"),
    path('',views.home,name="home"),
    path('puzzle',views.puzzle,name="puzzle"),
    path('hello',views.hello,name="hello"),
]
