# Generated by Django 2.2.4 on 2019-08-16 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0004_auto_20190813_0225'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VoteCount',
        ),
    ]
