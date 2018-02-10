from flask import Blueprint,render_template,redirect,request,Response,make_response,flash
from slackclient import SlackClient
import json

blueprint = Blueprint('slack',__name__)

from .config import BOT_TOKEN,SLACK_CLIENT_ID,SLACK_CLIENT_SECRET,SLACK_ADMIN_CHANNEL


@blueprint.route("login",methods=["GET","POST"])
def slacklogin():
    auth_code=request.args.get("code")
    auth_response=msg_response=im_response=""
    if auth_code:
        sc=SlackClient("")
        auth_response = sc.api_call(
        "oauth.access",
        client_id=SLACK_CLIENT_ID,
        client_secret=SLACK_CLIENT_SECRET,
        code=auth_code
        )
        try:
            username=auth_response["user"]["name"]
            userid=auth_response["user"]["id"]
            flash("Welcome {}".format(username))
        except KeyError:
            flash("An error has occurred")
    return render_template("slacklogin.html",auth=repr(auth_response),channel=repr(msg_response),im=repr(im_response))


def send_im(userid=None,channel=None,**kwargs):
        sc=SlackClient(BOT_TOKEN)
        log=kwargs.pop("log",[])
        if userid and not channel:
            msg_response= sc.api_call(
            "conversations.open",
            users=userid)
            channel=msg_response["channel"]["id"]
        admin_response= sc.api_call(
            "chat.postMessage",
            channel=channel,**kwargs)
        log.extend([msg_response,admin_response])

@blueprint.route('verifymember/<userid>')
def notify_admin_new_member(userid):
        log=[]
        send_im(userid=userid,
            text="Thankyou. Your application has been sent to the committee to be verified",
            log=log)
        send_im(
            channel=SLACK_ADMIN_CHANNEL,
            text="A new member has requested to join",
            attachments=[{
              "fallback":"New member request",
              "title":"New member application",
              "text":"<https://web.wostraq.net/showmember/{userid}|View info>".format(userid=userid),
              "callback_id":userid,
              "actions":[
                 {"name":"member","text":"Approve","value":"ok","type":"button"},
                 {"name":"member","text":"Reject","value":"reject","type":"button"}],
              "color":"info"}],
            log=log)
        return repr(log)

@blueprint.route("welcome/<userid>")
def welcome_new_member(userid):
    log=[]
    send_im(userid=userid,
        text="Welcome to WoSTRAQ",
        attachments=[{
              "fallback":"New member application",
              "title":"New member application",
              "text":"Please click the button below to start the application form",
              "callback_id":userid,
              "actions":[
                 {"name":"member","text":"Apply now","value":"apply","type":"button"}],
              "color":"info"}],
       log=log)
    return repr(log)





  

@blueprint.route("eventlistener",methods=['post'])
def eventlistener():
  content=request.get_json()
  event=content.get("event",content)
  if event["type"]=="url_verification":
     return event["challenge"]
  elif event["type"]=="team_join":
     welcome_new_member(event["user"]["id"])
     return "",200
  else:
     raise Exception(event["type"])

@blueprint.route("messagelistener",methods=['post'])
def messagelistener():

  payload=json.loads(request.form['payload'])
  actions={a["name"]:a["value"] for a in payload["actions"]}
  if actions["member"]=="ok":
    newattach={"text":"Approved by {}".format(payload["user"]["name"]),
               "color":"good"}
  elif actions["member"]=="reject":
    newattach={"text":"Rejected by {}".format(payload["user"]["name"]),
               "color":"danger"}
  elif actions["member"]=="apply":
    newattach={"text":"Displaying the form",
               "color":"info"}
    show_reg_form(payload["user"]["id"],payload["trigger_id"])
  else:
    newattach={"text":"Unknown instruction:{}".format(actions["member"]),
               "color":"danger"}  
  message=payload["original_message"]
  message["attachments"].append(newattach)
  for a in message["attachments"]:
    a.pop("actions",None)
  return json.dumps(message),200,{"Content-Type":"application/json"}


def show_reg_form(userid,triggerid):
    sc=SlackClient(BOT_TOKEN)
    sc.api_call("dialog.open",
    trigger_id= triggerid,
    dialog= {
        "callback_id": "ryde-46e2b0",
        "title": "Member Registration",
        "submit_label": "Register",
        "elements": [
            {
                "type": "text",
                "label": "Pickup Location",
                "name": "loc_origin"
            },
            {
                "type": "text",
                "label": "Dropoff Location",
                "name": "loc_destination"
            }
        ]
    }
    )
    
