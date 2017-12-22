from flask import Flask
from content import blueprint
def create_app():
  app=Flask('website')
  app.register_blueprint(blueprint,url_prefix='/')
  return app
  
  
