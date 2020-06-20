
# FullThrottle Labs - Backend Intern Assignment

This is a Production ready Django Web Application having Django-Rest API that serves a list of members(users) and their respective active periods. Active period basically includes the time at which member logs into the system(start_time) and logs out of the system(end_time). Custom management command to populate the database is also included.
Tech/framework used

    Python 3.8
    Django 3.0.6
    Postgres
    Django Rest Framework 3.11
    Markdown 3.2.2
    Django-Filter 2.2.0
    Psycopg2 2.8.5
    Python-decopule 3.2
    Pytz 2020.1
    sqlparse 0.3.1


## Currently Hosted at PythonAnywhere server: https://kanishkftltask.pythonanywhere.com/activity_record/members/ .



High level overview:

This Django project consists of one App:

    task

## It includes two models

1. User
2. ActivityPeriods

activityRecord is reponsible for serving the get request at the following mentioned API end-point by making queries to the database and performing serialization. This APP also stores the data related to the users active period like start time and end time.
account

For User models and its related operations.
Custom Management Command to populate the database

This command can be run by python manage.py populate_UserRecord .
Its code is present under activityRecord APP as follows activityRecord/management/commands/populate_UserRecord.py
Rest-API end-point

Get request for the list of members and their respective activity periods.

    /activity_record/members/

Response:

    ok is a json boolean field.
    members is a json array of Users
    Each User object has following fields id, real_name, tz(timezone) and activity_periods.
    activity_periods is again a json array of active time period.
    Each active time period has start_time and end_time fields.

{
    "ok": true,
    "members": [
        {
            "id": "a23a4474-32f5-42fe-8f82-ab495500ecf9",
            "real_name": "IYNQSFTFGP",
            "tz": "Africa/Djibouti",
            "activity": [
                {
                    "start_time": "June 20 2020 14:29",
                    "end_time": "July 20 2020 14:29"
                }
            ]
        },
        {
            "id": "5e27baf7-7393-447a-9a57-fc436d7e1f06",
            "real_name": "BWQURUNMKU",
            "tz": "US/Pacific",
            "activity": [
                {
                    "start_time": "June 20 2020 14:29",
                    "end_time": "July 20 2020 14:29"
                }
            ]
        },
        {
            "id": "0c9aafa2-75c6-47a4-aa0d-5b0eeea722d2",
            "real_name": "ECJLKFCBBQ",
            "tz": "Australia/Sydney",
            "activity": [
                {
                    "start_time": "June 20 2020 14:29",
                    "end_time": "July 20 2020 14:29"
                }
            ]
        },
        {
            "id": "1605c6da-e3cf-44c9-967d-f371fdf85372",
            "real_name": "MSLYNMIPVG",
            "tz": "Europe/Helsinki",
            "activity": [
                {
                    "start_time": "June 20 2020 14:29",
                    "end_time": "July 20 2020 14:29"
                }
            ]
        },
        {
            "id": "d8a7facd-8040-47a5-8d00-3642b35b5e7a",
            "real_name": "OZWRPOLVDK",
            "tz": "America/Argentina/La_Rioja",
            "activity": [
                {
                    "start_time": "June 20 2020 14:29",
                    "end_time": "July 20 2020 14:29"
                }
            ]
        },

Database Models used
User:

User models is an extention of AbstractUser model.
Having additional Fields as follow

    id (primary key, Char-field, fixed length 9)
    real_name (Char-field, max length 100)
    tz for timezone (Char-field, max length 100, default Asia/kolkata)

ActivityPeriod:

ActivityPeriod is a simple Django model having:

    user (Foreign Key User model)
    start_time (DateTimeField)
    end_time (DateTimeField)

Hosting locally:

Step-1: Clone the repo to your system.

Step-2: Download and install a PostgreSQL server, for ubuntu/debian users https://www.youtube.com/watch?v=M4RDizdaO9U

Step-3: Create new user and database in Postgres.

Step-4: Find evn_example.txt in the repo you just cloned, copy all text present in it to a new file, change all the fields in the text according to your Postgres setup and save this file as .env.
Make sure DEBUG is True for running locally.

Step-5: Find local_settings.example rename it as local_settings.py

Step-6: Run command: pip install -r requirements.txt

Step-7 Run command: python manage.py makemigrations

Step-8 Run command: python manage.py migrate

Step-9 Run command: python manage.py populate_UserRecord

Step-10 Run command: python manage.py runserver
Using Cloud services like AWS or PythonAnywhere

    Make sure DEBUG is False
    ALLOWED_HOST is configured according to usecase
    command: python manage.py collectstatic for collecting all the static files in the folder mentioned in STATIC_ROOT, you can change it if want to server static from other location

API View

Class based API for serving get request. Here get function first makes a query to database for all the User model and than pass the List of all Users to the the UserSerializer

class FetchDetails(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def list(self,request,format=None):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response({'ok':True,'members':serializer.data})

Custom Management Command to populate the database

This command fills the database with the dummy data.
command: python manage.py populate x
where x will be how many dummy objects we want to create . (ex:- python3 manage.py populate 10)
Command will be creating  User objects and each user will have 3 activity periods.
For random string generation, I have used ''.join(random.choices(string.ascii_uppercase, k=10))
TimeZone(tz) by a tuple of already provided timezones by pytz
Code is present under activityRecord APP as follows activityRecord/management/commands/populate_UserRecord.py
