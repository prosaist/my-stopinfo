#!/usr/bin/env python3
import urllib.request, urllib.parse, json, os
from datetime import datetime
from yandex_transport_webdriver_api import YandexTransportProxy

proxy = YandexTransportProxy('127.0.0.1', 25555)
path = os.path.dirname(os.path.realpath(__file__))
params = json.load(open('%s/params.json' % (path)))

def send(message):
    sms = 'https://sms.ru/sms/send?api_id=%s&to=%s&json=1&msg=%s' % (params['api_id'], params['phone'], message)
    with urllib.request.urlopen(sms) as response:
        data = json.loads(response.read().decode())
    return
message = ''
hour = datetime.now().time().hour
stop_url = params['stop_urls'][0 if hour < 13 else 1]
data = proxy.get_stop_info(stop_url['url'])
for transports in data['data']['transports']:
    name = transports['name']
    Types = transports['Types']
    if name in params['tramways'] and 'tramway' in Types:
        message += '%0a' + urllib.parse.quote(name) + '>'
        for thread in transports['threads']:
            for event in thread['BriefSchedule']['Events']:
                if 'Estimated' in event:
                    message += event['Estimated']['text'] + ';'
len = len(message)
if len > 1 and len < 160:
    send(message)
