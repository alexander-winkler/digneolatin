import requests

wikidata_endpoint = "https://query.wikidata.org/sparql"
query = """
SELECT ?authorLabel ?title ?year 
WHERE {
  ?book wdt:P407 wd:Q397.
  ?book wdt:P31 wd:Q7725634 .
  ?book wdt:P50 ?author.
  ?book wdt:P1476 ?title. 
  ?book wdt:P577 ?year.
  FILTER ( year(?year) > 1600 ).
  FILTER ( year(?year) < 1800 ).
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
   }
  }
 
        """

parameters = {
        'query' : query,
        'format' : 'JSON'
        }

headers = {"Accept" : "application/json"}

res = requests.get(wikidata_endpoint,headers=headers,params=parameters)

print(res.text)

