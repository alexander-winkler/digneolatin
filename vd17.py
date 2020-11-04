import requests

vd17_endpoint = "http://sru.k10plus.de/vd17"
parameters = {
        'version' : '1.1',
        'operation' : 'searchRetrieve',
        'recordSchema' : 'marcxml',
        'query' : 'pica.jah=1640 and pica.vlo=Nürnberg and pica.spr="lat"',
        'maximumRecords' : '10',
        }

print(requests.get(vd17_endpoint, params=parameters).text)
