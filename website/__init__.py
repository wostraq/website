from flask import Flask
from .views import home,about
def create_app():
  app=Flask('website')
  app.register_blueprint(home,url_prefix='/')
  app.register_blueprint(about,url_prefix='/about')
  return app
  
  
