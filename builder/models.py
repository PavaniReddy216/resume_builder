from django.db import models

class PersonalDetails(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    linkedin = models.CharField(max_length=150)
    github=models.CharField(max_length=150)
    address = models.TextField(max_length=50)
    Strength=models.TextField(max_length=50)
    hobbies=models.TextField(max_length=50)

class Education(models.Model):
    personal_details = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

class Experience(models.Model):
    personal_details = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    job_description = models.TextField()

class Skills(models.Model):
    personal_details = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)

class Internship(models.Model):  # Ensure this is properly defined
    personal_details = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.role} at {self.company_name}"
