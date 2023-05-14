import requests
import json
from app import get_db_connection

# Define SPARQL query to retrieve movie data
query = """
SELECT ?item ?itemLabel ?imdb_id ?date_of_release
WHERE 
{
  ?item wdt:P31 wd:Q11424;
        wdt:P577 ?date_of_release;
        wdt:P345 ?imdb_id.
  FILTER(YEAR(?date_of_release) > 2013)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
"""

# Define API endpoint and parameters
endpoint = "https://query.wikidata.org/sparql"
params = {
    "format": "json",
    "query": query
}

# Send GET request to API endpoint and get response
response = requests.get(endpoint, params=params)
data = json.loads(response.text)

# Print retrieved data
print(json.dumps(data, indent=4))


conn = get_db_connection()
cursor = conn.cursor()

for item in data['results']['bindings']:
    item_id = item['item']['value'].split('/')[-1]
    item_label = item['itemLabel']['value']
    imdb_id = item['imdb_id']['value']
    date_of_release = item['date_of_release']['value']

    cursor.execute('''
        INSERT INTO movies (item_id, item_label, imdb_id, date_of_release)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(item_id) DO UPDATE SET item_label=excluded.item_label, imdb_id=excluded.imdb_id, date_of_release=excluded.date_of_release
    ''', (item_id, item_label, imdb_id, date_of_release))
    
conn.commit()
cursor.close()
conn.close()