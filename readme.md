## Project Description

App which will fetch data from 3 services:
- money.py
- wnp.pl
- bankier.pl

Project stack:
- Django
- BeautifulSoup - parsing html
- Celery - Task queue
- RabbitMQ - Message Broker

<br/>

### To run app in development, install required packages via pipenv and type:
```
python manage.py runserver
```
<br/>

### Before you run application, you need data to show:

##### RabbitMQ(message broker)

Run RabbitMQ via Docker (you need su privileges):
```
docker run -d -p 5672:5672 rabbitmq
```

##### Celery

Run celery worker along with rabbitMQ:
```
celery -A project worker --loglevel=INFO
```
  
Open python shell and run task:
```
python manage.py shell
> from backend.tasks import *
# run every task
> fetch_bankier_data.delay()
> fetch_wnp_data.delay()
> fetch_money_data.delay()
```
<br/>
You will see in Celery terminal window tasks have been succeeded:

```
[2020-12-31 08:52:09,792: INFO/ForkPoolWorker-2] Task backend.tasks.fetch_bankier_data[8751b547-9aaf-4e2b-ad9f-b441b6216438] succeeded in 1.4489655389998006s: None
```

##### Periodic tasks

To be up to date, you can use periodic tasks (fetch new data every 2h), type:
```
celery -A project beat --loglevel=INFO
```