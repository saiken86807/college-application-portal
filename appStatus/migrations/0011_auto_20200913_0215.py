# Generated by Django 3.1 on 2020-09-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStatus', '0010_auto_20200912_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
