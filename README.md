dj-tornado
==========

![travis build status](https://travis-ci.org/weargoggles/django-tornado.svg?branch=master)

Embedding a production-ready HTTP server in your Django application by installing an app - easy as Py!

Simply install dj-tornado

```bash
pip install dj-tornado
```

Add it to your INSTALLED_APPS

```python
INSTALLED_APPS = (
  ...,
  
  'dj_tornado',
  
  ...,
)
```

And then run it directly

```bash
python manage.py tornadoserver
```

or in a Procfile

```yaml
web: python manage.py tornadoserver
```
