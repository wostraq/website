from flask import Blueprint,render_template,redirect,request,Response

blueprint = Blueprint('content',__name__)

@blueprint.route('/')
def home():
  return render_template('index.html')
  
@blueprint.route('about/membership')
def about_membership():
  return render_template('about_membership.html')

@blueprint.route('about/local')
def about_local():
  return render_template('about_local.html')

@blueprint.route('about/committee')
def about_committee():
  return render_template('about_committee.html')

@blueprint.route('projects/previous')
def projects_previous():
  return render_template('previousprojects.html')


@blueprint.route('projects/propose')
def projects_propose():
  return render_template('proposeproject.html')

@blueprint.route('about/join_us')
def join_us():
  return redirect('https://docs.google.com/forms/d/e/1FAIpQLSeWsC7onQ0yuk95MMHhunDw4UigOu6eVtjoPApZB7R-v3czdg/viewform')

from functools import wraps


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'wostraq' and password == 'password'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Data entry forms"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@blueprint.route('data_collection')
@requires_auth
def data_collection():
    return redirect('https://goo.gl/forms/hF7ai0d1xzXjbnCn2')



  
