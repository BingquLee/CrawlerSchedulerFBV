from django.db import models


# Create your models here.
class Users(models.Model):
    uid = models.CharField(max_length=128, primary_key=True)
    session_id = models.CharField(max_length=128, blank=False)

    class Meta:
        db_table = 'users'
