import requests
from lxml import etree
import matplotlib
import matplotlib.pyplot as plt

def query_vd17(year):
    vd17_endpoint = "http://sru.k10plus.de/vd17"
    parameters = {
            'version' : '1.1',
            'operation' : 'searchRetrieve',
            'recordSchema' : 'marcxml',
            'query' : f'pica.jah={str(year)} and pica.vlo=Nürnberg and pica.spr="lat"',
            'maximumRecords' : '10',
            }
    return requests.get(vd17_endpoint, params=parameters)
    
publication_numbers = []
years = range(1601,1699)
for year in years:
    root = etree.fromstring(query_vd17(year).content)
    hits = root.find('{http://www.loc.gov/zing/srw/}numberOfRecords').text
    publication_numbers.append(int(hits))

fig, ax = plt.subplots()
ax.bar(years,publication_numbers)
ax.set(xlabel='Year', ylabel='Books published',
               title='Latin books published in Nuremberg in the 17th century')
fig.savefig("vd17_nuremberg.png")
plt.show()

