# REST API build with Django

This project aims to build a REST API using Django and Django REST Framework.

## Dependencies

All of configurations have been made using Linux OS (Kubuntu-18.04 LTS). Package names could change between distributions.

This project required Graphviz to generate UML Class Diagram.

```bash
  sudo apt install graphviz
```

This project use Python 3.6 and virtualenv to manage its environment.

```bash
  sudo apt install python3.6 python3-venv python3-pip
  sudo python3 -m pip install venv
```

Only Python 3.6 has been tested but the project may be compliant with latest releases.

During documentation building, the README in Markdown format is converted to ReStructured Text unsing Pandoc.

```bash
  sudo apt install pandoc
```

To build documentation in pdf format, you need to have the following packages installed on your system:

* texlive-latex-recommended
* texlive-fonts-recommended
* texlive-latex-extra
* latexmk

```bash
  sudo apt install texlive-latex-recommended texlive-fonts-recommended texlive-latex-extra latexmk
```

## Build your dev environment

```bash
  python3 -m venv env
  source env/bin/activate
  (env) pip install -r requirements.txt
```

## Update your dev environment

```bash
  python3 -m venv env
  source env/bin/activate
  (env) pip install ....

  # adding sed command to fix a small issue with a package in the list
  (env) pip freeze | sed '/pkg-resources==0.0.0/d' | cat &> requirements.txt
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

## Deploy on Heroku

In local, you will need psycopg2 package but it triggers some installing issues.
To fix these issues, install a specific version of this package: `psycopg2==2.7.7`.

For deployment on Heroku server, this fix blocks the process. Remove psycopg2==2.7.7 line in `requirements.txt` before pushing branch on heroku.

```bash
(env) pip freeze | sed -e '/pkg-resources==0.0.0/d' -e '/psycopg2==2.7.7/d' | cat &> requirements.txt
```


## Generate UML Class Diagram

```bash
  (env) python manage.py graph_models --pydot -a -g -o /path/to/directory/app_uml_class_diagram.png
```

## Build documentation

[Sphinx](http://www.sphinx-doc.org/en/master/) framework is used to generate the project documentation.

```bash
  (env) cd docs
  (env) make html
```

### Automatic Documentation generation

Using the command `make doc` all technical documentation is automatically generated and added to the project documentation.

```bash
  (env) cd docs
  (env) make doc
```

1. Generate automatically technical doc from sources (output in `docs/api/` folder)
2. Inject it into special part of documentation (see `apidoc.rst` file)
3. Generate UML Class Diagram and include it too
4. Convert README.md to ReST using pandoc and add it at the root part of documentation

## Documentation of REST API for Developpers

### Generating OpenAPI schema

```bash
  (env) python manage.py generateschema &> openapi-schema.yml
```

In this project it is automatically done when calling the url `/openapi`.

### Create a user to log in

```bash
  (env) python manage.py createsuperuser
  # change password:
  (env) python manage.py changepassword <username>
```


### Swagger and ReDoc automatic REST API documentation

You will find 3 pssibilities to browse and test this REST API:

* Built-in web pages: just open the root url into a web browser and you will have basic web page to browse and test the API
* [Swagger UI](https://swagger.io/) page: `/swagger-ui/`
* [ReDOc](https://github.com/Redocly/redoc) page : `/redoc/`
