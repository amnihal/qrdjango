# Generated by Django 5.0.1 on 2024-01-21 07:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="puzzle",
            old_name="col",
            new_name="divID",
        ),
        migrations.RemoveField(
            model_name="puzzle",
            name="row",
        ),
    ]