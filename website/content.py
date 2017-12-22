from flask import Blueprint,render_template

blueprint = Blueprint('content')

@blueprint.route('/')
def home():
  return render_template('index.html')
  
@blueprint.route('/about')
def about():
  return render_template('about.html')
  
