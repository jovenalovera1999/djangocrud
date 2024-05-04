from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.

class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True)
    gender = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.gender

    class Meta:
        db_table = 'genders'

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55)
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    birth_date = models.DateField()
    contact_number = models.CharField(max_length=55)
    email_address = models.EmailField(max_length=55)
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def save(self):
        if not self.pk:
            self.password = make_password(self.password)
        
        super(User, self).save()