# Generated by Django 5.0.4 on 2024-04-25 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_forumpost_op_alter_forumpost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 25, 3, 28, 5, 741369)),
        ),
    ]
