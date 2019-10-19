from django.urls import path
from travello import views

app_name='travello'

urlpatterns=[
    path('',views.index)
]