# Generated by Django 3.2.9 on 2021-11-01 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_auto_20211101_1401"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="upvote",
            new_name="upvotes",
        ),
    ]