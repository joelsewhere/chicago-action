import shapefile
from shapely.geometry import Point, shape
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Chicago Action")



def address_search(address):
    try:
        location = geolocator.geocode(address)
    except: 
        return None

    point = (location.longitude,location.latitude) # an x,y tuple
    shp = shapefile.Reader('app/data/geo_export_b5da5f85-2fb8-4c09-8fa1-0efcdd152087.shp') #open the shapefile
    all_shapes = shp.shapes() # get all the polygons
    all_records = shp.records()
    for i in range(len(all_shapes)):
        boundary = all_shapes[i] # get a boundary polygon
        if Point(point).within(shape(boundary)): # make a point and see if it's in the polygon
            name = all_records[i][2] # get the second field of the corresponding record
            return name
    return None