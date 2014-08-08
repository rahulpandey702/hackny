from flask import Flask, redirect, url_for, session, request, render_template
from flask_oauth import OAuth
import urllib2
import json

SECRET_KEY = 'development key'
DEBUG = True
FACEBOOK_APP_ID = ''
FACEBOOK_APP_SECRET = ''


app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))


@app.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    me = facebook.get('/me')
    l = facebook.get('/me/likes')
    user = 'mandeep0405'
    url = 'http://ex.fm/api/v3/user/'+user+'/loved'
    
    res = [] 
    v = 'f'
    for like in l.data['data']:
        inn=[]
        inn.append(like['category'])
        inn.append(like['name'])        
        res.append(inn)
        
    jam ='http://api.jambase.com/search?band=Wilco&apikey=v4byef43z7pukkwjf6mu8ce9'    
    return render_template('hello.html',res=res)
    #return render_template('hello.html')
    #data = json.load(urllib2.urlopen(url))
    #result = []
    #for songs in data[songs]:
       #result.add(songs['title'])		
    #return result     		
	#print urlib("http://ex.fm/api/v3/user/mandeep0405/loved") 
	#return 'Logged in as id=%s name=%s redirect=%s' % \
    #    (me.data['id'], l.data['name'], request.args.get('next'))


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')


if __name__ == '__main__':
    app.run()
