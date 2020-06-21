
# FullThrottle Labs - Backend Intern Assignment

This is a Production ready Django Web Application having Django-Rest API that serves a list of members(users) and their respective active periods. Active period includes the time at which member logs into the system(start_time) and logs out of the system(end_time). Custom management command to populate the database is also included.

## Tech/framework used

    Python==3.6.9
    asgiref==3.2.10
    Django==3.0.7
    django-rest-framework==0.1.0
    djangorestframework==3.11.0
    pytz==2020.1
    sqlparse==0.3.1


## Currently Hosted at PythonAnywhere server: http://pallavagarwal.pythonanywhere.com/fetch/



In depth overview:

This Django project consists of one App:

    task

## It includes two models

1. User
2. ActivityPeriods

app is reponsible for serving the get request at the following mentioned API end-point by making queries to the database and performing serialization. 
This APP also stores the data related to the users active period like start time and end time and user details

Custom Management Command have been used to populate the database

This command can be run by **python manage.py populate 10** .
Its code is present under task app as follows task/management/commands/populate.py

## Rest-API end-point

Get request for the list of members and their respective activity periods.

    /fetch/

Response:

    ok is a json boolean field.
    members is a json array of Users
    Each User object has following fields id, real_name, tz(timezone) and activity.
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
            "id": "efd0f3d5-d114-4148-873b-06eeba214312",
            "real_name": "ZWFBHSNFFI",
            "tz": "America/Belize",
            "activity": [
                {
                    "start_time": "June 20 2020 14:50",
                    "end_time": "July 20 2020 14:50"
                },
                {
                    "start_time": "June 20 2020 14:50",
                    "end_time": "July 20 2020 14:50"
                },
                {
                    "start_time": "June 20 2020 14:50",
                    "end_time": "July 20 2020 14:50"
                }
            ]
        },
        {
            "id": "db0e9ba1-a274-432a-b367-920c77c10e04",
            "real_name": "ZGSLYXBDJA",
            "tz": "Asia/Singapore",
            "activity": [
                {
                    "start_time": "June 20 2020 14:50",
                    "end_time": "July 20 2020 14:50"
                },
                {
                    "start_time": "June 20 2020 14:50",
                    "end_time": "July 20 2020 14:50"
                },
                {
                    "start_time": "June 20 2020 14:50",
                    "end_time": "July 20 2020 14:50"
                }
            ]
        },


I have paste the snippet for differently populated activityperiods value as 1st one has only 1 record while second one has 3 acitvity records

## Database Models used

User:

Having Fields as follow

    id (primary key, uuid-field, unique=true)
    real_name (Char-field, max length 100)
    tz for timezone (Char-field, max length 100,)

ActivityPeriod:

ActivityPeriod is a simple Django model having:

    member (Foreign Key to User model)
    start_time (DateTimeField)
    end_time (DateTimeField)

Hosting locally:

Step-1: Clone the repo to your system.

Step-2: run virtualenv -p python3 env

Step-3: run pip install -r requirements.txt 

Make sure DEBUG is True for running locally.

Step-7 Run command: python manage.py makemigrations

Step-8 Run command: python manage.py migrate

Step-9 Run command: python manage.py populate 10

Step-10 Run command: python manage.py runserver

Steps for Cloud services in this case hosted on PythonAnywhere

    Make sure DEBUG is False
    ALLOWED_HOST is configured according to usecase
    command: python manage.py collectstatic for collecting all the static files in the folder mentioned in STATIC_ROOT

# API View

Class based API for serving get request. Here get function first makes a query to database for all the User model and than pass the List of all Users to the the UserSerializer

class FetchDetails(ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    def list(self,request,format=None):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response({'ok':True,'members':serializer.data})
        
 Alternatively we can use function based view as well as viewsets to serve the same purpose:-
 
 using function based view:-
 
 @api_view(['GET'])
 
    def fetch_details(request):
        user = User.objects.all()
        user_list = []
        for i in range(len(user)):
            serializer = UserSerializer(user[i])
            user_list.append(serializer.data)
        return Response({'ok':True,'members':user_list})
        
 Using viewsets:-
 
 class FetchDetails(ModelViewSet):
 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def list(self,request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many=True)
        return Response({'ok':True,'members':serializer.data})

# Custom Management Command to populate the database

This command fills the database with the dummy data.

command: **python manage.py populate x**

where x will be how many dummy objects we want to create . (ex:- python3 manage.py populate 10)

Command will be creating  User objects and each user will have 3 activity periods.

Custome command file **populate.py** resides at **task/management/commands/populate.py

For random string generation, I have used **''.join(random.choices(string.ascii_uppercase, k=10))

TimeZone(tz) by a tuple of already provided timezones by pytz

Ps :- I haven't made two seperated apps for user and activity cause it was mentioned to make one app, though i know it is better practise to have two seperate apps for user and other things
