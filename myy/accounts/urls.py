from django.urls import path

from accounts import views

app_name='accounts'

urlpatterns=[
    path('reg/',views.Register,name='reg'),
    path('login/', views.login_page, name='login'),
    path('logout/',views.logout_page, name='logout'),
    path('contact/',views.contact_view,name='contact')
]