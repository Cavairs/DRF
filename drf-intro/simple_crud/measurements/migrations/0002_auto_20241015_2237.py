# Generated by Django 3.1.2 on 2024-10-15 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]