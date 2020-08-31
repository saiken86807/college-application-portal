from django.db import models

# Create your models here.


class Applicant(models.Model):
    MAJOR = (
        ('Veterinary Technology', 'Veterinary Technology'),
        ('Equine Studies', 'Equine Studies'),
        ('Interactive Media Design', 'Interactive Media Design'),
        ('Emerging Media & Content Creation', 'Emerging Media & Content Creation'),
        ('Applied Computer Science', 'Applied Computer Science'),
        ('Criminal Justice', 'Criminal Justice'),
        ('Nursing', 'Nursing'),
        ('Psychology, Mental Health Counseling',
         'Psychology, Mental Health Counseling'),
    )

    SCHOOL = (
        ('Boston Latin School', 'Boston Latin School'),
        ('Sturgis Charter Public School', 'Sturgis Charter Public School'),
        ('Hopkinton High School', 'Hopkinton High School'),
        ('Advanced Math and Science Academy', 'Advanced Math and Science Academy'),
        ('Dover-Sherborn Regional High School',
         'Dover-Sherborn Regional High School'),
        ('Mystic Valley Regional Charter School',
         'Mystic Valley Regional Charter School'),
        ('Lexington High School', 'Lexington High School'),
        ('Weston High School', 'Weston High School')
    )

    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    major = models.CharField(max_length=200, null=True, choices=MAJOR)
    school = models.CharField(max_length=200, null=True, choices=SCHOOL)
    GPA = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Denied', 'Denied')
    )

    applicant = models.ForeignKey(
        Applicant, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)


# class DecisionStatus(models.Model):
