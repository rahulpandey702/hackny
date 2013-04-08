import foursquare
from flask import Flask
from flask import request
app = Flask(__name__)

client = foursquare.Foursquare(client_id='VUZAK0IZX2HY0ME2YO0ZS1XFELNRQ00VZEJOHPRBP4XMLSPG', client_secret='HB4YDNBEPHRDUDLEMVNHFULAFPS1WDIOLTVAVQFNPESZKT1F', redirect_uri='http://ec2-50-19-38-82.compute-1.amazonaws.com/redirect')
@app.route("/")
def test():
    # Construct the client object
    # Build the authorization url for your app
    auth_uri = client.oauth.auth_url()
    return auth_uri

@app.route("/redirect")
def redirect() :
    code = request.args.get('code')
    f = open('myfile','w')
    f.write('hi there\n')
    f.close()
    access_token = client.oauth.get_token(code)
    # Apply the returned access token to the client
    #client.set_access_token(access_token)

    # Get the user's data
    #user = client.users()
    return code


if __name__ == "__main__":
    app.run()
