from flask import Blueprint
blueprint = Blueprint('git',__name__)
import subprocess,uwsgi

@blueprint.route("pull",methods=["GET","POST"])
def git_pull():
    try:
      output=subprocess.check_output(["/usr/bin/git","pull"])
      success="Operation successful"
      uwsgi.reload()
    except subprocess.CalledProcessError as e:
      success="Operation failed"
      output=e.output
    return "{}\n{}".format(success,output)
