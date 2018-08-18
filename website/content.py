from flask import Blueprint,render_template,redirect,request,Response,make_response,flash
import json

blueprint = Blueprint('content',__name__)

@blueprint.route('/')
def index():
   return redirect('/index.html')

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'wostraq' and password == 'password'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(render_template('access_denied.html'), 401,
    {'WWW-Authenticate': 'Basic realm="Data entry forms"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@blueprint.route("unavailable")
def unavailable():
    return "Not available offline"

