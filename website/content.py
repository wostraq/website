from flask import Blueprint,render_template,redirect,request,Response,make_response,flash
import json,csv

blueprint = Blueprint('content',__name__)

@blueprint.route('/')
@blueprint.route('index.html')
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

@blueprint.route('about/curriculum')
def about_curriculum():
  return render_template('about_curriculum.html')

@blueprint.route('projects/previous')
def projects_previous():
  with open("ponvcontacts.csv") as f:
   dr=list(csv.DictReader(f))
   names=list({r['Name'] for r in dr})
   names.sort(key=lambda i:i.split()[-1])
   nameslist=[(n,"\n".join(["{},{}".format(r["Role"],r["Hospital"]) for r in dr if r["Name"]==n])) for n in names]
  return render_template('previousprojects.html', nameslist=nameslist)


@blueprint.route('projects/propose')
def projects_propose():
  return render_template('proposeproject.html')

@blueprint.route('projects/proposals')
def projects_propose():
  return render_template('proposals.html')

@blueprint.route('about/join_us')
def join_us():
  return redirect('https://docs.google.com/forms/d/e/1FAIpQLSeWsC7onQ0yuk95MMHhunDw4UigOu6eVtjoPApZB7R-v3czdg/viewform')

@blueprint.route('ext/membersarea')
def membersarea():
  return redirect('https://forum.wostraq.net')

from functools import wraps


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

@blueprint.route('data_collection')
@requires_auth
def data_collection():
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLScduKaCJBaFZKllZP8ON14aWik9ZRFG1UBMUnloZp22j-AqRw/viewform')

@blueprint.route("cache.appcache")
def appcache():
    return "not found",404
    cache=['/index.html',"/about/local","/about/committee","about/membership","/projects/previous","/projects/propose"]
    cache.extend("https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css /static/css/style.css https://fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic,700italic https://code.jquery.com/jquery-1.12.0.min.js https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js".split())
    fallback=["/ /unavailable"]
    import os
    out=["CACHE MANIFEST","#{}".format(os.path.getmtime(__file__))]
    out.append("CACHE:")
    out.extend(cache)
    out.append("FALLBACK:")
    out.extend(fallback)
    rs=make_response("\n".join(out))
    rs.headers["Content-Type"]="text/cache-manifest"
    return rs


@blueprint.route("unavailable")
def unavailable():
    return "Not available offline"

@blueprint.before_request
def flashmessages():
    for msg in request.args.getlist('flash'):
        flash(msg)
