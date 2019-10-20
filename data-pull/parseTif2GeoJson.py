import gdal
import json

filename = 'IND_births_pp_v2_2015.tif'
ds = gdal.Open(filename)

width = ds.RasterXSize
height = ds.RasterYSize

band = ds.GetRasterBand(1)
arr = band.ReadAsArray()
[cols, rows] = arr.shape

gt = ds.GetGeoTransform()

stepX = gt[1]
stepY = gt[5]

with open('birth-dump.json', 'w') as birthDump:
    geoDict = {
        'type': 'FeatureCollection',
        'features': []
    }

    for y, row in enumerate(arr):
        for x, col in enumerate(row):
            coords = [stepX*x + gt[0], stepY*y + gt[3]]
            pointDict = {}
            pointDict['type'] = 'Feature'
            pointDict['geometry'] = {
                'type': 'Point',
                'coordinates': coords
            }
            pointDict['properties'] = str(arr[y,x]) 
            geoDict['features'].append(pointDict)
    json.dump(geoDict,birthDump)
