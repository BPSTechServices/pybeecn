import matplotlib.pyplot as plt
import geopandas
import os
import jupyter
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as graph_objs

def view(args):
    """
    Test BEECN Location Viewer
-------------------------------------------------------------
Add description of the BEECN CLI tool and commands here

-------------------------------------------------------------
    :param args:
    :return:
    """


    data_dir = os.path.join(args.directory, 'data_files')
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    url = 'https://opendata.arcgis.com/datasets/6e6185533d5447deb8b7204c27e1858e_92.geojson'
    url1 = 'https://opendata.arcgis.com/datasets/9f50a605cf4945259b983fa35c993fe9_125.geojson'
    df_grid = geopandas.read_file(url1)
    df_points = geopandas.read_file(url)



    print(df_grid)


    f, ax = plt.subplots(figsize=(10,10))
    df_grid.plot(ax=ax, color='green')
    # df_points.plot(color='blue', ax=ax)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('BEECN Locations in Portland, OR')

    if args.show:
            plt.show()


