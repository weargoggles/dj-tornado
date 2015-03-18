dj-tornado
==========

![travis build status](https://travis-ci.org/weargoggles/dj-tornado.svg?branch=master)
![pypi release](https://img.shields.io/pypi/v/dj-tornado.svg)

Embedding a production-ready HTTP server in your Django application by installing an app - easy as Py!

dj-tornado uses [dj-static](https://github.com/kennethreitz/dj-static) to serve your dynamic pages and your static assets with [tornado](https://github.com/tornadoweb/tornado)'s great non-blocking HTTP server.

Setup
-----

Simply install dj-tornado

```bash
pip install dj-tornado
```

Add it to your INSTALLED_APPS

```python
INSTALLED_APPS = (
  ...,
  'dj_tornado',
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
