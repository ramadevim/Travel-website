from django.urls import path

from myapp import views

app_name='myapp'

urlpatterns=[
      path('',views.hello),
      path('add',views.add)
]