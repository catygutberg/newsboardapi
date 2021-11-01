from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
import sys

from api.models import Post


def reset_post_upvotes():
    Post.objects.all().update(upvotes=0)


def start():
    scheduler = BackgroundScheduler(timezone="Europe/Kiev")
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(
        reset_post_upvotes,
        "interval",
        hours=24,
        name="reset_post_upvotes",
        jobstore="default",
        id="reset_post_upvotes",
        replace_existing=True,
    )
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
