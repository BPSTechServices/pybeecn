import requests
import matplotlib.pyplot as plt
import geopandas
import os
import jupyter
import descartes
import json
from shapely.geometry import mapping, shape
import pandas as pd
from pandas.io.json import json_normalize
import plotly.plotly as py
import plotly.figure_factory as ff

def view(args):
    """
    Test BEECN Location Viewer
-------------------------------------------------------------
Add description of the BEECN CLI tool and commands here

-------------------------------------------------------------
    :param args:
    :return:
    """
    # url =
    url = 'https://opendata.arcgis.com/datasets/6e6185533d5447deb8b7204c27e1858e_92.geojson'
    url1 = 'https://opendata.arcgis.com/datasets/9f50a605cf4945259b983fa35c993fe9_125.geojson'
    grid = geopandas.read_file(url1)
    points = geopandas.read_file(url)

    ddir = os.path.join(args.directory, 'data_files')
    if not os.path.exists(ddir):
        os.mkdir(ddir)
    print(type(grid))
    print(type(points))

    # print(grid.head())
    # print(list(grid))
    # print(list(points))
    # print(grid['NAME'].unique())
    # print(points['SITE_NAME'].unique())

    # grid['POPULATION'] = []
    for i in grid['NAME']:
        print(i)


    f, ax = plt.subplots(figsize=(10,10))
    grid.plot(ax=ax)
    points.plot(color='green', ax=ax)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('BEECN Locations in Portland, OR')

    jupyter

    if args.show:
        plt.show()






