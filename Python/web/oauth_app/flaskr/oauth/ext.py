from flask_login import LoginManager
from flaskr.config.utils import getenv
from authlib.integrations.flask_client import OAuth


oauth = OAuth()

login_manager = LoginManager()


def redirect_authorize(redirect_uri):
    oauth.register(
        name='google',
        client_id=getenv('GOOGLE_CLIENT_ID'),
        client_secret=getenv('GOOGLE_CLIENT_SECRET'),
        server_metadata_url=getenv('GOOGLE_DISCOVERY_URL'),
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    return oauth.google.authorize_redirect(redirect_uri)

def get_userinfo():
    token = oauth.google.authorize_access_token()
    return oauth.google.parse_id_token(token)
