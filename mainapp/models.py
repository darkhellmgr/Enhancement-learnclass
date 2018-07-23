from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('1', 'Male'),
    ('0', 'Female'),
)

IMP_CHOICES = (
    ('Nepal', 'Nepal'),
    ('Bhutan', 'Bhutan'),
    ('Sweden', 'Sweden'),
)


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=False)
    password = models.CharField(max_length=100, blank=False)
    street_address = models.IntegerField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20, blank=True)
    government_identification = models.CharField(max_length=20, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    dob = models.DateTimeField(max_length=8)
    subject_of_interest = models.CharField(max_length=200, blank=True, null=True)
    special_care_needed = models.CharField(max_length=1, choices=(
        ('1', 'Yes'),
        ('0', 'No')
    ))


class School(models.Model):
    title = models.CharField(max_length=200, blank=False)
    street_address = models.CharField(max_length=200, blank=False)
    postal_code = models.CharField(max_length=10, blank=False)
    city = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=100, choices=IMP_CHOICES)
    phone = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # QUIZ MODEL


class SchoolAdmin(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=False)
    password = models.CharField(max_length=100, blank=False)
    street_address = models.IntegerField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20, blank=True)
    government_identification = models.CharField(max_length=20, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    # grade = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=400, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class EditCourse(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=400, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class QuizSubjectiveQuestion(models.Model):
    question = models.CharField(max_length=200)


class McqQuiz(models.Model):
    question = models.CharField(max_length=200)
    option = models.CharField(max_length=200)

