from django.core.management.base import BaseCommand, CommandError
import os
import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling


class Command(BaseCommand):
    help = '''runs your application in tornado's HTTPServer'''

    def handle(self, *args, **kwargs):
        # Bind to PORT if defined, otherwise default to 5000.
        port = int(os.environ.get('PORT', 5000))
        application = Cling(get_wsgi_application())
        container = tornado.wsgi.WSGIContainer(application)
        http_server = tornado.httpserver.HTTPServer(container)
        http_server.listen(port)
        try:
            tornado.ioloop.IOLoop.instance().start()
        except KeyboardInterrupt:
            raise CommandError('Terminating server on request')


