from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
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
STATUS = (
    ('Received', 'Received'),
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Denied', 'Denied')
)
SUBMISSION = (
    ('Not Submitted', 'Not Submitted'),
    ('Submitted', 'Submitted')
)


class Application(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    major = models.CharField(max_length=200, blank=True,
                             null=True, choices=MAJOR)
    school = models.CharField(
        max_length=200, blank=True, null=True, choices=SCHOOL)
    GPA = models.FloatField(null=True, blank=True, validators=[
                            MinValueValidator(2), MaxValueValidator(4)])
    status = models.CharField(
        max_length=200, blank=True, null=True, choices=STATUS, default='Received')
    app_submitted = models.CharField(
        max_length=25, blank=True, null=True, choices=SUBMISSION, default='Not Submitted')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
