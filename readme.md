### Project Description

App which will fetch data from 3 services:
- money.py
- wnp.pl
- bankier.pl

Supposed software used in project:
- Django
- BeautifulSoup - parsing html
- Celery - Task queue
- RabbitMQ - Message Broker

<br/>

##### To run app in development, install required packages via pipenv and type:
```
python manage.py runserver
```
<br/>

##### To check how celery tasks work:

Run RabbitMQ via Docker (you need su privileges):
```
docker run -d -p 5672:5672 rabbitmq
```

Run celery worker:
```
celery -A project worker --loglevel=INFO
```
  
Open python shell and run task:
```
python manage.py shell
> from backend.tasks import *
# run any task, for example:
> fetch_bankier_data.delay()
```
<br/>

##### To run periodic tasks (fetch new data every 2h), type:
```
celery -A project beat --loglevel=INFO
```