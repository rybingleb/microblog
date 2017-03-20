import os

CSRF_ENABLED = True
SECRET_KEY = 'da1s465456S4S58VFRH54dE54g8f74G5G46s'
OIDC_ID_TOKEN_COOKIE_SECURE = False

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'rybingleb'
MAIL_PASSWORD = 'ZXCqwe789ASD'

# administrator list
ADMINS = ['rybingleb@gmail.com']

LANGUAGES = {
    'en': 'English',
    'ru': 'Русский'
}


TRANSLATE_YANDEX_API_KEY = 'trnsl.1.1.20170317T105950Z.6e000cc3eaaeb75b.98b320fa49c6dc7fbd8ea565f01ceb6762509c3b'