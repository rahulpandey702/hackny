from flask import Flask
from flask import request
import foursquare
app = Flask(__name__)

#Localhost
client = foursquare.Foursquare(client_id='IMLKPLRVC03LS1XD354X5D0OA2NH0UMYXLN2BXOJEJFJTU3H', client_secret='W50OBJNVCWV2ZA5CYPQGRKKTDCBPR0NAFPTGX2SVWDJCLXII', redirect_uri='http://localhost:5000/redirect')

#client = foursquare.Foursquare(client_id='VUZAK0IZX2HY0ME2YO0ZS1XFELNRQ00VZEJOHPRBP4XMLSPG', client_secret='HB4YDNBEPHRDUDLEMVNHFULAFPS1WDIOLTVAVQFNPESZKT1F', redirect_uri='http://ec2-50-19-38-82.compute-1.amazonaws.com/redirect')
@app.route("/")
def test():
    # Construct the client object
    # Build the authorization url for your app
    auth_uri = client.oauth.auth_url()
    return auth_uri

@app.route("/redirect")
def redirect() :
    code = request.args.get('code')
    access_token = client.oauth.get_token(code)
    # Apply the returned access token to the client
    #client.set_access_token(access_token)

    # Get the user's data
    #user = client.users()
    return code


if __name__ == "__main__":
    app.run()
