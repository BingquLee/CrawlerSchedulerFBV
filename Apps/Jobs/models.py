from django.db import models


# Create your models here.
class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    channel = models.CharField(max_length=32, blank=False)
    account = models.CharField(max_length=32, blank=False)
    publish_time = models.CharField(max_length=32, blank=False)
    publish_freq = models.CharField(max_length=16)
    text = models.TextField(max_length=4096, blank=True, null=True)
    file_amount = models.IntegerField(blank=False)
    status = models.BooleanField(blank=False)
    update_ts = models.BigIntegerField(blank=False)
    update_dt = models.DateField(blank=False)

    def to_json(self):
        dic = self.__dict__
        if "_sa_instance_state" in dic:
            del dic["_sa_instance_state"]
        return dic

    class Meta:
        db_table = 'jobs'


class Files(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128, blank=False)
    channel = models.CharField(max_length=32, blank=False)
    account = models.CharField(max_length=32, blank=False)
    status = models.BooleanField(blank=False)

    def to_json(self):
        dic = self.__dict__
        if "_sa_instance_state" in dic:
            del dic["_sa_instance_state"]
        return dic

    class Meta:
        db_table = 'files'


class Account(models.Model):
    account_id = models.CharField(max_length=128, primary_key=True)
    session_id = models.CharField(max_length=128, blank=False)
    channel = models.CharField(max_length=128, blank=False)

    class Meta:
        db_table = 'accounts'
