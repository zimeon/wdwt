#!/usr/bin/env python
""" Get and extract data from Wikidata SPARQL endpoint.

https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual#SPARQL_endpoint
"""
import requests

sparql_url = "https://query.wikidata.org/sparql"

query = """
SELECT DISTINCT ?item ?itemLabel WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
  {
    SELECT DISTINCT ?item WHERE {
      ?item p:P106 ?s .
      ?s (ps:P106/(wdt:P279*)) wd:Q11518247.
    }
    LIMIT 100
  }
}
"""

r = requests.post(sparql_url, data={'query': query, 'format': 'json'})
print(r.text)
