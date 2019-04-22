import os
import shutil
import logging.config
from . import beecn as bn
import pandas as pd
import geopandas as gpd
logger = logging.getLogger(__name__)


def view(args):
    """
    Test BEECN Location Viewer
-------------------------------------------------------------
Add description of the BEECN CLI tool and commands here

-------------------------------------------------------------
    :param args:
    :return:
    """
    # Create the directory structure.
    beecn_dir = bn.create_beecn_dir(args.directory)

    # Create plots folder to store images/plots
    plot_dir = os.path.join(beecn_dir, 'plots_dir')
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)
    else:
        shutil.rmtree(plot_dir)
        os.makedirs(plot_dir)

    # Create vis_data folder to store vis_data files
    data_dir = os.path.join(beecn_dir, 'data_dir')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    else:
        shutil.rmtree(data_dir)
        os.makedirs(data_dir)

    # todo: get this plot to show populations by size.
    beecn_geo = 'https://opendata.arcgis.com/datasets/6e6185533d5447deb8b7204c27e1858e_92.geojson'
    neighborhood_geo = 'https://opendata.arcgis.com/datasets/9f50a605cf4945259b983fa35c993fe9_125.geojson'
    bn.plot_beecn_png(beecn_geo, neighborhood_geo, plot_dir, show=args.show if args.show else False)

    population_csv = args.filePath
    column=args.column
    bn.plot_beecn_html(neighborhood_geo, plot_dir, beecn_geo, population_csv, population_column=column)

    # bn.plot_beecn_html(neighborhood_geo, plot_dir, population_csv, population_column='White alone (NHoL)').add_to(m)

