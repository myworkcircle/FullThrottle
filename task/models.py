from django.db import models
from django.utils import timezone
import uuid
import pytz
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')

    def __unicode__(self):
        return self.id

class ActivityPeriods(models.Model):
    members = models.ForeignKey(User,related_name='activity',on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    
