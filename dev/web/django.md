# Django dev tip

## Model

### specifying database to use

In the site setting file, find the data base setting

### specifing the table name of a model class

In the meta class, define the db_table propertuy like the following:

```python
db_table = 'music_album'
```

### Generating Model from existing tables

```
python manage.py  inspectdb
```

This command will generate the python code of the
Model classes, copy them to the applications and
change the managed field in the meta class to `True`
or simply remove it, and then run

```
python manage.py migrate
```

### mapping a model to a created table

If you have created a table and just want to map to it,
if you run `python manage.py migrate`, it will complain
that the table already exists.

In this case, run the following command:

```python
python manage.py migrate --fake <appname>
```

### fields

#### DateTimeField

http://stackoverflow.com/questions/2771676/django-datetime-issues-default-datetime-now

```
date = models.DateTimeField(auto_now_add=True, blank=True)
```

#### CharField

#### ForeignField

1. Define a foreign key to it self

    parentId = models.ForeignKey("self")

or
    parentId = models.ForeignKey("CategoryModel")


### querying using model objects

we can use fields to do queries on the model class.
But If we want to query using the fields of a related object
by foreign key, we need to use `__` to as field separator.

E.g

    Entry.objects.filter(pub_date__year=2006)

Is to filter on the entries where the the year of pub_date,
which is a related object is 2006

### relation ship

#### many to many

#### one to many

How to access the set of related objects from the `many side`?
Django adds a special property in the many side, `<relation_name>_set`
all in lower case[^1].

## View

### Simple view

In its simplest case, a view is just a function that takes at least `HttpRequest`
as argument. The following is an example:

```python
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

### Capturing  arguments

### Generic View

### Template


## URLConfig, the controller that connect user request to views

In the project folder and each app folder, there is a file called
`urls.py`, which is responsible for controlling dispatching user request
to the views defined in the project. `urls.py` looks like this:

```
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]

```

The elements defined in urlpatterns are the `routing rules`.
When there is a request from the user,django framework will
extract the url(the part excluding the host) and match it against
each element in this list and dispatch the request to the view in the
second part.

You can also dispatch it to another urls definition. the first line
uses `include` directive to do so.

## Django RESTful framework

## Filter

https://django-filter.readthedocs.io/en/latest/usage.html
http://www.django-rest-framework.org/api-guide/filtering/

## run django with uwsgi and nginx

### Serving static files

#### Setting up STATIC_URL

`STATIC_URL` is the part that will be appended to the urls when accessing static files.

#### Setting up STATIC_ROOT

`STATIC_ROOT` is the directory where the static files will be output by `manage.py collectstatic`

#### setting up rules in nginx

    location /static/  {
        alias /path/to/static/;
    }

### uploading files

## admin app

### Filtering by foreign key fields

in the admin class of the model class, add an item in the filter_list the format
`<relation_field_name>__<field_name_in_the_related_class>`

## celery

https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/

## debug

When debug is turned off in settings.py, by default admin is not allowed to be accessed,
we need to setup allowed hosts in `ALLOWED_HOSTS`


## other tips



## references
* [Django get started](https://docs.djangoproject.com/en/1.10/intro/)
* http://stackoverflow.com/questions/25924858/django-1-7-migrate-gets-error-table-already-exists
* [How To Serve Django Applications with uWSGI and Nginx on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-14-04)
* [https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-16-04](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-16-04)
* [Setting up Django and your web server with uWSGI and nginx](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
* [nginx not serving admin static files?](http://serverfault.com/questions/403264/nginx-not-serving-admin-static-files)
* [Managing static files (e.g. images, JavaScript, CSS)](https://docs.djangoproject.com/en/dev/howto/static-files/#deploying-static-files-in-a-nutshell)
* [ALLOWED HOSTS](https://docs.djangoproject.com/en/1.9/ref/settings/#allowed-hosts)
* [Django self-referential foreign key](http://stackoverflow.com/questions/15285626/django-self-referential-foreign-key)

[^1]: http://stackoverflow.com/questions/19799955/django-get-the-set-of-objects-from-many-to-one-relationship
