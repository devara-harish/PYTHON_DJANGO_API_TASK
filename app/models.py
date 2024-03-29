from django.db import models

# Create your models here.



# We are creating tables for perticular columns
# For each and every model we performing some operations
# address field we dealing with One_TO_one_Field 
# Work experience,project,qualifications, we are dealing with many to many fields


class Address(models.Model):
    hno = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class WorkExperience(models.Model):
    company_name = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    address = models.CharField(max_length=100)

    
class Qualifications(models.Model):
    qualification_name = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    percentage = models.FloatField()
    

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField()
   

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=15)
    address_details = models.OneToOneField(Address, on_delete=models.CASCADE)
    work_experience = models.ManyToManyField(WorkExperience)
    qualifications = models.ManyToManyField(Qualifications)
    projects = models.ManyToManyField(Project)
    photo = models.ImageField()

