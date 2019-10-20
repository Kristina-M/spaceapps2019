import requests
import json
from elasticsearch import Elasticsearch, helpers, ElasticsearchException
import pdb

pmm_url = "https://pmmpublisher.pps.eosdis.nasa.gov/opensearch"
# init ES connector
esClient = Elasticsearch()


def get_geoJson_link(dataset, date):
    # Construct request
    # Only want one item at a time
    # API searches from end date to start date. Hardcode early start date
    # HARD CODED INDIA DATASET LAT LON
    params = {
        'q': dataset,
        'lat': '25', 
        'lon': '78',
        'limit': '1',
        'startTime': '2000-01-01',
        'endTime': date
    }
    headers = {
        'accept': 'Application/json'
    }
    res = requests.get(pmm_url, headers=headers, params=params)
    if res.status_code != 200:
        print("ERROR: {} - {}".format(res.status_code, res.text))
        return None
    res_json = res.json()
    if res_json['totalItems'] != 1:
        print("WARN: No data entries found")
        return None
    # extract geoJson download url from
    url = res_json['items'][0]['action'][1]['using'][1]['url']
    return url

# def remove_geoJson_properties(d):
#    return {k:v for k,v in d.iteritems() if k is 'properties'}

def format_es_geoshape_collection(json, date):
    for shape in json['features']:
        shape['properties']['date'] = date
    return json

def es_upload_geoJson_from_url(url, date, index):
    # download geoJson
    headers = {
        'accept': "application/json"
    }
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        return None
    pdb.set_trace()
    # es cant handle nested properties so use custom hook
#     geoJson = json.loads(res.text, object_hook=remove_geoJson_properties) 
    geoJson = format_es_geoshape_collection(res.json(), date)
    # bulk upload
    try:
        helpers.bulk(esClient, geoJson, index=index, doc_type='geo_shape')
    except ElasticsearchException as ese:
        print(ese)
    return
 

##########
# MAIN SCRAPING FUNCTION FOR NASA PMM
# To be called for periodic updates of database
# Inputs:
#    dataset: dataset label specified by PMM
##########
def scrape_pmm(dataset, date, index):
    url = get_geoJson_link(dataset, date)
    if url is None:
        print("Faied to pull url")
        return
    es_upload_geoJson_from_url(url, date, index) 
    return

if __name__ == '__main__':
    # TODO: Set up as background app with scheduled tasks for periodic data scraping
    scrape_pmm('global_landslide_nowcast', '2019-09-01', 'test-geojson-landslide')
