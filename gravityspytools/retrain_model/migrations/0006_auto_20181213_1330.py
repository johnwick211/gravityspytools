# Generated by Django 2.1.3 on 2018-12-13 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retrain_model', '0005_newclass_processed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newclass',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]