from django.db import models
import uuid


class File(models.Model):
    """ Model for Files """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,)
    name = models.CharField(max_length=150)
    file_path = models.FileField()
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

