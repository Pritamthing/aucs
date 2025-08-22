from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from .models import User, CleanupReport

@shared_task
def cleanup_inactive_users():
    print(f"Coming up")
    threshold_days = int(getattr(settings, "INACTIVITY_THRESHOLD_DAYS", 30))
    threshold_date = timezone.now() - timedelta(days=threshold_days)

    inactive_users = User.objects.filter(last_login__lt=threshold_date, is_active=True)
    deleted_count = inactive_users.count()
    inactive_users.delete()

    active_count = User.objects.filter(is_active=True).count()
    print(f"active count ->{active_count}")

    report = CleanupReport.objects.create(
        users_deleted=deleted_count,
        active_users_remaining=active_count
    )
    print(f"report saved ->{report.id}")

    # return f"Deleted {deleted_count} users, {active_count} active users remain and report: {report.id}."
