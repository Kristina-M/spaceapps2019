import json
from math import cos
from PIL import Image


with open(imgFilename, 'rb') as imgFile:
    img = Image.open(imgFile)
    imgX, imgY = img.size

imgFilename = 'inFile.png' 
inRegionData = 'via_region_data.json'
imgExtension = '8020693'
imgWidthMeters = 3470
scale = imgWidthMeters/imgX  # number of meters per px

latList = [26, 59, 35]
longList = [81, 31, 27] 

centreLat = latList[0] + latList[1]/60 + latList[2]/(60**2)
centreLong = longList[0] + longList[1]/60 + longList[2]/(60**2)

M_PER_DEG_LAT = (111132.954 - 559.822*cos(2*centreLat) \
    + 1.175*cos(4*centreLat))
M_PER_DEG_LONG = (111132.954 * cos (centreLong))

with open(inRegionData, "r") as jsonFile:
    jsonData = json.load(jsonFile)
    
    regions = jsonData[imgFilename + imgExtension]['regions']
    communities = {}
    for i, region in enumerate(regions.values()):
        shape = region['shape_attributes']
        x_points = shape['all_points_x']
        y_points = shape['all_points_y']
        
        polygon = []
        for j in range(len(x_points)):
            lat, lng = convert(x_points[j], y_points[j])
            polygon.append(
                {'lat': lat + centreLat,
                 'lng': lng + centreLng} 
            ) 
        communities['Community' + str(i)] = polygon

with open('polydump.json', 'w') as dumpFile:
    json.dump(communities, dumpFile)
