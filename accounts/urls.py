from django.urls import path
from .views import LoginView, MeView, RefreshView, AdminStatsView, UserSummaryView

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/refresh/', RefreshView.as_view(), name='refresh'),
    path('auth/me/', MeView.as_view(), name='me'),

    path('admin/stats/', AdminStatsView.as_view(), name='admin-stats'),
    path('user/summary/', UserSummaryView.as_view(), name='user-summary'),
]
