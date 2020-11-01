from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class Role(models.Model):
    '''
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    '''
    
    name = models.CharField(max_length=50, default=1)

    def __str__(self):
        return self.name
        
class MyUser(AbstractUser):
    """ Base model for patient
    and doctor """

    #ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,)

    #Role
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    #Personal
    middle_name = models.CharField(max_length=50)
    age = models.IntegerField()
    blood_type = models.CharField(max_length=50, blank=True, null=True)

    #Contact Details
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)

    #Address
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    barangay = models.CharField(max_length=50)
    postal_code = models.IntegerField()

    #System
    date_created = models.DateTimeField(
                    auto_now=True, blank=True, null=True
                    )
    date_updated = models.DateTimeField(
                    auto_now_add=True, blank=True, null=True
                    )
    active_status = models.BooleanField(
                    default=True, blank=True, null=True
                    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return f'{self.id}'