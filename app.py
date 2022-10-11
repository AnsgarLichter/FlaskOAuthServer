from website.app import create_app

app = create_app({
    'SECRET_KEY': 'secret',
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite',
    'OAUTH2_REFRESH_TOKEN_GENERATOR': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'AUTHLIB_INSECURE_TRANSPORT': 1
})