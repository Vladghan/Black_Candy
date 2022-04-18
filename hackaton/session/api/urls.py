from django.urls import path

from session.api import views

urlpatterns = [
    path('sessions/', views.SessionView.as_view()),
    path('session/<int:pk>/', views.SessionDetailView.as_view()),
    path('sessions_data/', views.SessionDataView.as_view()),
    path('user_session/<int:pk>/', views.SessionDataDetailView.as_view()),
]
