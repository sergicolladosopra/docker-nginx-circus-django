[circus]
statsd = {{ CIRCUS_STATSD | default('True') }}
httpd = {{ CIRCUS_HTTPD | default('False') }}

[watcher:webapp]
cmd = /usr/local/bin/chaussette --fd $(circus.sockets.web) app.wsgi.application
numprocesses = 3
use_sockets = True

[socket:web]
host = 127.0.0.1
port = 9999

[env:webapp]
PYTHONPATH = /opt/app
