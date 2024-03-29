from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sign-in/', views.SendSignInEmail.as_view(), name='sign_in'),
    path('sign-out/', views.sign_out, name='sign_out'),
    path('verify-email/<uidb64>/<token>/', views.verify_email, name='verify_email'),
]

htmx_urlpatterns = [
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('subscribe-only/', views.subscribe_only, name='subscribe_only'),   
]

urlpatterns += htmx_urlpatterns