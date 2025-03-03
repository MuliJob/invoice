"""cLIENTS mODELS"""
from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    """Clients Model"""
    name = models.CharField(max_length=255)
    email = models.EmailField()
    id_number = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    contact_reference = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="clients", on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    
    def __str__(self):
        """Object name"""
        return '%s' % self.name
