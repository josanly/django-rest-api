# REST API build with Django 

## Build your dev environment

```bash
  python3 -m venv env              
  source env/bin/activate
  pip install -r requirements.txt
```

## Launch local server

If it is the first time you run the server locally, you need to initiate the database.

```bash
  (env) python manage.py migrate
```

Start the server locally by default: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

```bash
  (env) python manage.py runserver    
```

Or you can specify the address and port:

```bash
  (env) python manage.py runserver <ipaddr>:<port>
  (env) python manage.py runserver <port>
```

