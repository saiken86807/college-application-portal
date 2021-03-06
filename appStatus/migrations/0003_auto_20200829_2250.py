# Generated by Django 3.1 on 2020-08-29 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStatus', '0002_application_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='application',
        ),
        migrations.AddField(
            model_name='applicant',
            name='gpa',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='major',
            field=models.CharField(choices=[('Veterinary Technology', 'Veterinary Technology'), ('Equine Studies', 'Equine Studies'), ('Interactive Media Design', 'Interactive Media Design'), ('Emerging Media & Content Creation', 'Emerging Media & Content Creation'), ('Applied Computer Science', 'Applied Computer Science'), ('Criminal Justice', 'Criminal Justice'), ('Nursing', 'Nursing'), ('Psychology, Mental Health Counseling', 'Psychology, Mental Health Counseling')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='school',
            field=models.CharField(choices=[('Boston Latin School', 'Boston Latin School'), ('Sturgis Charter Public School', 'Sturgis Charter Public School'), ('Hopkinton High School', 'Hopkinton High School'), ('Advanced Math and Science Academy', 'Advanced Math and Science Academy'), ('Dover-Sherborn Regional High School', 'Dover-Sherborn Regional High School'), ('Mystic Valley Regional Charter School', 'Mystic Valley Regional Charter School'), ('Lexington High School', 'Lexington High School'), ('Weston High School', 'Weston High School')], max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]
