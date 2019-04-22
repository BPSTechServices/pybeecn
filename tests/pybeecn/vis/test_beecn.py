"""
This work was authored by Gabriel McBride in support 
of Portland Open Data Program and Portland Bureau of 
Emergency Management BEECN Program. The effort was 
conducted as a use case for the student's masters 
project to study the interaction between Systems 
Engineering and Data Science activities.
"""
import os
import pybeecn.vis.beecn as bn
import shutil
import logging.config
import pandas as pd
logger = logging.getLogger(__name__)


def test_create_beecn_dir():
    directory = os.path.join('/tmp', 'test_beecn_files')
    bn.create_beecn_dir(directory)
    assert os.path.exists(directory)
    logger.info('{} exists'.format(directory))
    shutil.rmtree(directory)
    logger.info('test complete...removing {}'.format(directory))


def test_beecn_lat_long():
    beecn_geo = 'https://opendata.arcgis.com/datasets/6e6185533d5447deb8b7204c27e1858e_92.geojson'
    beecn_df = bn.beecn_lat_long(beecn_geo)
    assert isinstance(beecn_df, pd.DataFrame)
    assert len(beecn_df.columns) == 11


def test_plot_beecn_png():
    beecn_url = 'https://opendata.arcgis.com/datasets/6e6185533d5447deb8b7204c27e1858e_92.geojson'
    neighborhood_url = 'https://opendata.arcgis.com/datasets/9f50a605cf4945259b983fa35c993fe9_125.geojson'
    plot_dir = os.path.join('/tmp', 'plot_dir')
    os.makedirs(plot_dir)
    bn.plot_beecn_png(beecn_url, neighborhood_url, plot_dir)

    assert os.path.getsize(plot_dir) > 0
    logger.info('{} directory has size {}'.format(plot_dir, os.path.getsize(plot_dir)))
    logger.info('removing the directory {} and files'.format(plot_dir))
    shutil.rmtree(plot_dir)


def test_plot_beecn_html():
    plot_dir = os.path.join('/tmp', 'plot_dir')
    population_csv = os.path.join(os.path.dirname(__file__), 'vis_data/neighborhood_population.csv')
    neighborhood_geo = 'https://opendata.arcgis.com/datasets/9f50a605cf4945259b983fa35c993fe9_125.geojson'
    beecn_geo = 'https://opendata.arcgis.com/datasets/6e6185533d5447deb8b7204c27e1858e_92.geojson'
    assert os.path.exists(population_csv)

    os.makedirs(plot_dir)
    bn.plot_beecn_html(neighborhood_geo, plot_dir, beecn_geo,population_csv)

    assert os.path.getsize(plot_dir) > 0
    logger.info('{} directory has size {}'.format(plot_dir, os.path.getsize(plot_dir)))
    logger.info('removing the directory {} and files'.format(plot_dir))
    shutil.rmtree(plot_dir)
