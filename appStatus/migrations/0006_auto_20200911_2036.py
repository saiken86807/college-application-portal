# Generated by Django 3.1 on 2020-09-11 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStatus', '0005_auto_20200903_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='GPA',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
