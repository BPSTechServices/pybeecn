import requests
import matplotlib.pyplot as plt
import geopandas

from pybeecn.vis.beecn import getPolyCoords
import descartes
import json
from shapely.geometry import mapping, shape
import pandas as pd
from pandas.io.json import json_normalize

def view(args):
    """
    Test BEECN Location Viewer
-------------------------------------------------------------
Add description of the BEECN CLI tool and commands here

-------------------------------------------------------------
    :param args:
    :return:
    """
    #
    url = 'https://opendata.arcgis.com/datasets/6e6185533d5447deb8b7204c27e1858e_92.geojson'
    url1 = 'https://opendata.arcgis.com/datasets/9f50a605cf4945259b983fa35c993fe9_125.geojson'
    grid = geopandas.read_file(url1)
    points = geopandas.read_file(url)
    print(points['geometry'].head(1))
    print(grid['geometry'].head(1))

    # grid['x'] = grid.apply(getPolyCoords, geom='geometry', coord_type='x', axis=1)
    # grid['y'] = grid.apply(getPolyCoords, geom='geometry', coord_type='y', axis=1)

    # points['x'] = points.apply(getPolyCoords, geom='geometry', coord_type='x', axis=1)
    # points['y'] = points.apply(getPolyCoords, geom='geometry', coord_type='y', axis=1)


    f, ax = plt.subplots()
    grid.plot(ax=ax)
    points.plot(color='green', ax=ax)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('BEECN Locations in Portland, OR')
    plt.show()






