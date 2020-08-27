import pyproj
from pyproj import CRS

def updater(crs):
    crs_utm = CRS.from_user_input(int(crs))
    return crs_utm.name
