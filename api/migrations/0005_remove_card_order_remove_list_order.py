# Generated by Django 4.1.3 on 2022-11-11 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_card_options_alter_list_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="card",
            name="order",
        ),
        migrations.RemoveField(
            model_name="list",
            name="order",
        ),
    ]
