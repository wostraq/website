from flask import Blueprint,render_template,redirect,request,Response,make_response,flash
from slackclient import SlackClient
import json

blueprint = Blueprint('slack',__name__)

from .config import BOT_TOKEN,ADMIN_TOKEN,CHANNELS,SLACK_CLIENT_ID,SLACK_CLIENT_SECRET,SLACK_ADMIN_CHANNEL
from . import db

class memberdb(db.Model):
    userid=db.Column(db.String(20),primary_key=True)
    membertype=db.Column(db.String(10))
    base=db.Column(db.String(10))
    grade=db.Column(db.String(10))
    active=db.Column(db.Boolean())
    emailconsent=db.Column(db.String(3))
@blueprint.route("setup")
def setup():
    db.create_all()
    return "OK"
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
        else:
            msg_response={}
        admin_response= sc.api_call(
            "chat.postMessage",
            channel=channel,**kwargs)
        log.extend([msg_response,admin_response])

@blueprint.route('verifymember/<userid>')
def notify_admin_new_member(userid,newmember=True):
        log=[]
        send_im(userid=userid,
            text="Thankyou. Your application has been sent to the committee to be verified",
            log=log)
        send_im(
            channel=SLACK_ADMIN_CHANNEL,
            text={True:"A new member has requested to join",False:"A member has updated their details"}[newmember],
            attachments=[{
              "fallback":{True:"New member request",False:"Member updated details"}[newmember],
              "title":"Member details",
              "text":"<@{userid}>".format(userid=userid),
              "callback_id":"vet-{}".format(userid),
              "actions":[
                 {"name":"member","text":"Check","value":"check","type":"button"},
                 {"name":"member","text":"Accept","value":"ok","type":"button"},
                 {"name":"member","text":"Reject","value":"reject","type":"button"}],
              "color":"info"}],
            log=log)
        return repr(log)

from io import StringIO
@blueprint.route("welcome/<userid>")
@blueprint.route("welcome",methods=["POST"])
def welcome_new_member(userid=None):
    log=[]
    kwargs=dict(
        text="Welcome to WoSTRAQ",
        attachments=[{
              "fallback":"New member application",
              "title":"New member application",
              "text":"Please click the button below to start the application form",
              "callback_id":"updatebtn-{}".format(userid or request.form["user_id"]),
              "actions":[
                 {"name":"member","text":"Apply now","value":"apply","type":"button"}],
              "color":"info"}]
       )
    if userid is None:
       sc=SlackClient(BOT_TOKEN)
       log.append(sc.api_call("chat.postEphemeral",
         user=request.form["user_id"],
         channel=request.form["channel_id"],
         **kwargs))
       with open("postmessage","w") as f:
         f.write(repr(log))
       return "",200
    else:
        send_im(userid=userid,log=log,**kwargs)

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
  command,userid=payload['callback_id'].split('-')
  user_is_me=(payload["user"]["id"]==userid)
  if command=="vet":
    user=memberdb.query.filter(memberdb.userid==userid).one()
    actions={a["name"]:a["value"] for a in payload["actions"]}
    if actions["member"]=="check":
        show_reg_form(userid,payload["trigger_id"])
        return "",200
    if actions["member"]=="ok":
      newattach={"text":"Approved by {}".format(payload["user"]["name"]),
               "color":"good"}
      user.active=True
      sc=SlackClient(ADMIN_TOKEN)

      for chn in [CHANNELS.get(user.membertype,None),CHANNELS.get(user.base,None)]:
         sc.api_call("groups.invite",
            channel=chn,
            user=user.userid)
      db.session.add(user)
      db.session.commit()
    elif actions["member"]=="reject":
      newattach={"text":"Rejected by {}".format(payload["user"]["name"]),
               "color":"danger"}
  elif command=="updatebtn":
    show_reg_form(payload["user"]["id"],payload["trigger_id"])
    return "",200
  elif command=="regform":
    newmember=memberdb(userid=userid,**payload['submission'])
    membertype={"st":"full","co":"cons"}.get(newmember.grade[:2],"assoc")
    if user_is_me:
      notify_admin_new_member(userid)
    db.session.merge(newmember)
    db.session.commit()
    return "",200
  else:
    newattach={"text":"Unknown instruction received",
               "color":"danger"}  
  message=payload["original_message"]
  message["attachments"].append(newattach)
  for a in message["attachments"]:
    a.pop("actions",None)
  return json.dumps(message),200,{"Content-Type":"application/json"}


def show_reg_form(userid,triggerid,callback_cmd="regform"):
    user=memberdb.query.filter(memberdb.userid==userid).one_or_none()
    if not user: 
      user=memberdb()
      submitbutton="Register"
      title="Member Registration"
    else:
      submitbutton="Update"
      title="Change details"
    sc=SlackClient(BOT_TOKEN)
    dialog =sc.api_call("dialog.open",
    trigger_id= triggerid,
    dialog= {
        "callback_id": "{}-{}".format(callback_cmd,userid),
        "title": title,
        "submit_label": submitbutton,
        "elements": [
            {
                "type": "select",
                "label": "Base hospital Feb 2018",
                "name": "base",
                "value":user.base,
                "options":[
                   {"label":"Ayr","value":"ayr"},

                   {"label":"Crosshouse","value":"xh"},
                   {"label":"Dumfries and Galloway","value":"dgri"},

                   {"label":"Forth Valley","value":"fvrh"},

                   {"label":"Glasgow Royal Infirmary","value":"gri"},
                   {"label":"Hairmyres","value":"hm"},
                   {"label":"Inverclyde","value":"irh"},
                   {"label":"Monklands","value":"mk"},

                   {"label":"Queen Eliz Univ Hosp","value":"qeuh"},
                   {"label":"Royal Alexandra Hosp","value":"rah"},

                   {"label":"Wishaw","value":"wgh"}]



          },
            {
                "type": "select",
                "label": "Grade",
                "name": "grade",
                "value": user.grade,
                "options":[
                   {"label":"Consultant","value":"cons"},
                   {"label":"Specialty doctor","value":"nccg"},
                   {"label":"ST7","value":"st7"},
                   {"label":"ST6","value":"st6"},
                   {"label":"ST5","value":"st5"},
                   {"label":"ST4","value":"st4"},
                   {"label":"ST3/LAT","value":"st3"},
                   {"label":"CT2/ACCS/LAT","value":"st2"},
                   {"label":"CT1/ACCS/LAT","value":"st1"},
                   {"label":"FY1/FY2","value":"fy"},
                   {"label":"Student","value":"student"},
                   {"label":"Other","value":"other"}]

            },
          {
               "type":"select",
               "label":"Add to mailing list",
               "hint":"Add email to mailing list for teaching, courses etc. We will never share your email address with other parties without your consent",
               "name":"emailconsent",
               "value":user.emailconsent,
               "options":[
                 {"label":"Yes - add to list","value":"yes"},
                 {"label":"No - just for WoSTRAQ","value":"no"}
               ]
         }
        ]
    }
    )
