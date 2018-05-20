from flask import Flask
from . import content,slack,git
def create_app():
  app=Flask('website')
  app.register_blueprint(content.blueprint,url_prefix='/')
  app.register_blueprint(slack.blueprint,url_prefix='/slack/')
  app.register_blueprint(git.blueprint,url_prefix="/git/")

  app.config.from_object("website.config")
  return app
  
  
