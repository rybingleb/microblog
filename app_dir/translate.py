import http.client
import json
import urllib

from flask_babel import gettext

from config import TRANSLATE_YANDEX_API_KEY


def translate(text, sourceLang, destLang):
    print(TRANSLATE_YANDEX_API_KEY)
    if TRANSLATE_YANDEX_API_KEY == "":
        return gettext('Error: translation service not configured.')
    try:
        # translate
        conn = http.client.HTTPSConnection('translate.yandex.net')
        params = {
            'key': TRANSLATE_YANDEX_API_KEY,
            'text': text.encode('utf-8'),
            'lang': destLang
        }
        conn.request("POST", '/api/v1.5/tr.json/translate?' + urllib.parse.urlencode(params))

        resp = conn.getresponse().read()
        # print(resp)
        jresp = json.loads(resp)

        # print('2', jresp)
        # print(jresp['text'])
        # print(''.join(jresp['text']))

        return ''.join(jresp['text'])
    except:
        return gettext('Error: Unexpected error.')
