import foursquare
from flask import Flask
app = Flask(__name__)

@app.route("/")
def test():
    # Construct the client object
    client = foursquare.Foursquare(client_id='VUZAK0IZX2HY0ME2YO0ZS1XFELNRQ00VZEJOHPRBP4XMLSPG', client_secret='HB4YDNBEPHRDUDLEMVNHFULAFPS1WDIOLTVAVQFNPESZKT1F', redirect_uri='http://ec2-50-19-38-82.compute-1.amazonaws.com')
    #client = foursquare.Foursquare(client_id='VUZAK0IZX2HY0ME2YO0ZS1XFELNRQ00VZEJOHPRBP4XMLSPG', client_secret='HB4YDNBEPHRDUDLEMVNHFULAFPS1WDIOLTVAVQFNPESZKT1F', redirect_uri='http://fondu.com/oauth/authorize')
    # Build the authorization url for your app
    auth_uri = client.oauth.auth_url()
    return auth_uri

if __name__ == "__main__":
    app.run()
