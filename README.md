# test_task
test_task is a service for sending mailing lists

## Install

Сlone the repo 
```sh
git clone https://github.com/holistr/test_task
```

Install the dependencies

```sh
pip install requirements.txt
```

Rooll up migrations

```sh
python manage.py migrate
```
Create superuser

```sh
python manage.py createsuperuser
```

Run up

```sh
python manage.py runserver
```
