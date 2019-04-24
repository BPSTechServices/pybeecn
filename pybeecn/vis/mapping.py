import os
import shutil
import logging.config
from . import beecn as bn
import pandas as pd
import geopandas as gpd
logger = logging.getLogger(__name__)


def view_map(args):
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

    points_url = '{}'.format(args.points)
    boundary_url = '{}'.format(args.boundaries)

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

    bn.plot_beecn_png(points_url, boundary_url, plot_dir, show=args.show if args.show else False)

    population_csv = args.filePath
    column=args.column
    bn.plot_population_map_html(boundary_url,  points_url, plot_dir, population_csv, population_column=column)

    # bn.plot_beecn_html(neighborhood_geo, plot_dir, population_csv, population_column='White alone (NHoL)').add_to(m)

