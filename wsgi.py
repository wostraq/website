from flask import Flask

app = Flask("website")

#  Uncomment to use the middleware
#flaskbb.wsgi_app = ReverseProxyPathFix(flaskbb.wsgi_app)
