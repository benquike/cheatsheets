# Django dev tip

## Model

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

## references
*[Django get started](https://docs.djangoproject.com/en/1.10/intro/)
* http://stackoverflow.com/questions/25924858/django-1-7-migrate-gets-error-table-already-exists