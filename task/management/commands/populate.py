from django.core.management.base import BaseCommand, CommandError
from task.models import User,ActivityPeriods
from django.utils import timezone
from random import randint
from django.utils.crypto import get_random_string
import datetime as dt
import time
import pytz
import random
import string

TIMEZONES = tuple(pytz.all_timezones)


#creating dummy user and activityperiods model objects
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('total', type=int,help='Indicates total number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            user = User.objects.create(real_name= ''.join(random.choices(string.ascii_uppercase, k=10)),tz= random.choice(TIMEZONES))
            ActivityPeriods.objects.create(members=user,start_time=dt.datetime.now(),end_time=dt.datetime.now()+dt.timedelta(days=30))