# Generated by Django 3.1 on 2020-08-29 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appStatus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('major', models.CharField(choices=[('Veterinary Technology', 'Veterinary Technology'), ('Equine Studies', 'Equine Studies'), ('Interactive Media Design', 'Interactive Media Design'), ('Emerging Media & Content Creation', 'Emerging Media & Content Creation'), ('Applied Computer Science', 'Applied Computer Science'), ('Criminal Justice', 'Criminal Justice'), ('Nursing', 'Nursing'), ('Psychology, Mental Health Counseling', 'Psychology, Mental Health Counseling')], max_length=200, null=True)),
                ('school', models.CharField(choices=[('Boston Latin School', 'Boston Latin School'), ('Sturgis Charter Public School', 'Sturgis Charter Public School'), ('Hopkinton High School', 'Hopkinton High School'), ('Advanced Math and Science Academy', 'Advanced Math and Science Academy'), ('Dover-Sherborn Regional High School', 'Dover-Sherborn Regional High School'), ('Mystic Valley Regional Charter School', 'Mystic Valley Regional Charter School'), ('Lexington High School', 'Lexington High School'), ('Weston High School', 'Weston High School')], max_length=200, null=True)),
                ('gpa', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Denied', 'Denied')], max_length=200, null=True)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appStatus.applicant')),
                ('application', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appStatus.application')),
            ],
        ),
    ]
