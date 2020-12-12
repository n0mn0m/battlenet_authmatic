# config.py

from authomatic.providers import oauth2, oauth1

CONFIG = {
    'bz': {

        'class_': oauth2.Blizzard,
        'consumer_key': '',
        'consumer_secret': ''
    },

}
