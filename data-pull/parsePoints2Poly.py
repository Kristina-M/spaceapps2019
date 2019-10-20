import json

with open('vilPoly.json', 'r') as inJson:
    inDict = json.load(inJson)

geoDict = {
    'type': 'FeatureCollection',
    'features': []
}
for com in inDict.values():
    xAvg = 0
    yAvg = 0
    polyDict = {}
    polyDict['type'] = 'Feature'
    polyDict['geometry'] = {
        'type': 'Point',
    }
    for point in com:
        xAvg += point['lat']
        yAvg += point['lng']
    coord = [xAvg/len(com), yAvg/len(com)]
    polyDict['geometry']['coordinates'] = coord
    polyDict['properties'] = {'this': 1}

    geoDict['features'].append(polyDict)
with open('geoJson.json', 'w') as geoJson:
    json.dump(geoDict, geoJson)
