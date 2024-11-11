from django.urls import path
from . import views

urlpatterns = [
    path('', views.log, name='log'),  # Login page as the default route
    path('customiser_view/', views.customiser_view, name='customiser_view'),
    path('signup', views.signup, name='signup'),
    path('log', views.log, name='log'),  # Optional: Keep this if you need 'log' by name elsewhere
    path('logout_view/', views.logout_view, name='logout_view'),
    path('login_view/', views.login_view, name='login_view'),
    path('custom', views.custom, name='custom'),  # Custom view
]
