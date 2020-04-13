# REST API build with Django 

## Dependencies

This project required Graphviz to generate UML Class Diagram.

```bash
   sudo apt install graphviz
```

## Build your dev environment

```bash
  python3 -m venv env
  source env/bin/activate
  (env) pip install -r requirements.txt
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

## Generate UML Class Diagram

```bash
  (env) python manage.py graph_models --pydot -a -g -o docs/_static/images/app_uml_class_diagram.png
```
