# calculate area (sqkm) for given slope & distance thresholds
# using geopandas and rasterstats 
# (must be in separate script and imported to work in jupyter)

# import modules
from osgeo import gdal
import pandas as pd
import geopandas as gpd
from rasterstats import zonal_stats
from tqdm import tqdm
import math

# function to get pixel size from slope image and return area in sqkm per pixel
def get_pxl_size(img):
    raster = gdal.Open(img)
    gt = raster.GetGeoTransform()
    pxl_size = gt[1]
    area = pxl_size * pxl_size / 1000000
    return area

# get pixel size in sqkm 
pixel_area = get_pxl_size('outputs/slope_images/Auckland-slope.kea')

# define function to return pixel counts within geopandas polygon with rasterstats
def calcArea(geometry, img):
    area = geometry.area
    radius = str(round(math.sqrt(area/math.pi), -3)/1000) + 'km'
    slope_vals = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
    sum  = zonal_stats(geometry, img, categorical=True)[0]
    fua_dict = {}
    for slope in tqdm(slope_vals, leave=False):
        count = 0
        for key, value in sum.items():
            if key <= slope:
                count += value
        area = count * pixel_area
        fua_dict['u' + radius + '_u' + str(slope) + 'deg'] = area
    return fua_dict
