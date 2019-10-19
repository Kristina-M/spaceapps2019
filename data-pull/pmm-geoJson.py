import requests
import json
import pdb

pmm_url = "https://pmmpublisher.pps.eosdis.nasa.gov/opensearch"

def get_geoJson_link(dataset, date):
    # Construct request
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
        return None
    res_json = res.json()
    if res_json['totalItems'] != 1:
        return None
    # extract geoJson download url from
    return res_json['items'][0]['action'][1]['using'][1]['url']

def remove_geoJson_properties(d):
    return {k:v for k,v in d.iteritems() if k is not 'properties'}
    
def es_upload_geoJson_from_url(url):
    # download geoJson
    headers = {
        'accept': "application/json"
    }
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        return None
    # es cant handle nested properties so use custom hook
    geoJson = json.loads(res.text, object_hook=remove_geoJson_properties) 


if __name__ == '__main__':
    pdb.set_trace()
