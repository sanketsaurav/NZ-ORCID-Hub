# SEE: http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/
import sys
sys.path.insert(0, '/var/www/orcidhub')

from application import app as application
