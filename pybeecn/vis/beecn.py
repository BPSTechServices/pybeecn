"""
This work was authored by Gabriel McBride in support 
of Portland Open Data Program and Portland Bureau of 
Emergency Management BEECN Program. The effort was 
conducted as a use case for the student's masters 
project to study the interaction between Systems 
Engineering and Data Science activities. 
"""

import os
import logging.config
import shutil
import geopandas as gpd
import matplotlib.pylab as plt
logger = logging.getLogger(__name__)


def create_beecn_dir(directory):
    if not os.path.exists(directory):
        logger.info('creating directory {}...'.format(directory))
        os.makedirs(directory)
    else:
        logger.info('{} already exists...overwriting'.format(directory))
        shutil.rmtree(directory)
        os.makedirs(directory)
    return directory


def plot_beecns(beecn_url, neighborhood_url, plot_dir, show=False, figwidth=10, figheight=10, beecncolor='blue', neighborhoodcolor='green'):
    neighborhood_df = gpd.read_file(neighborhood_url)
    beecn_df = gpd.read_file(beecn_url)

    f, ax = plt.subplots(figsize=(figwidth, figheight))
    neighborhood_df.plot(ax=ax, color=neighborhoodcolor)
    beecn_df.plot(ax=ax, color=beecncolor)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('BEECN Locations in Portland, OR')
    if show:
        plt.show()
    f.savefig(os.path.join(plot_dir, 'beecn_locations.png'))
    return
