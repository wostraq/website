from flask import Blueprint,render_template

blueprint = Blueprint('content',__name__)

@blueprint.route('/')
def home():
  return render_template('index.html')
  
@blueprint.route('/about/membership')
def about_membership():
  return render_template('about_membership.html')

@blueprint.route('/about/local')
def about_local():
  return render_template('about_local.html')

@blueprint.route('/about/committee')
def about_committee():
  return render_template('about_committee.html')

@blueprint.route('/projects/previous')
def projects_previous():
  return render_template('previousprojects.html')


@blueprint.route('/projects/propose')
def projects_propose():
  return render_template('proposeproject.html')
  
