from django.urls import path
from .views import latest_report, trigger_cleanup, all_reports, users, register, health_check

urlpatterns = [
    path("reports/latest/", latest_report),
    path("health/", health_check),
    path("reports/list/", all_reports),
    path("users/list/", users),
    path("users/register/", register),
    path("cleanup/trigger/", trigger_cleanup),
]
