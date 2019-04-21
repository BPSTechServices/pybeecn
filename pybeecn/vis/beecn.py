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
import pandas as pd
import matplotlib.pyplot as plt
import folium
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


def plot_beecn_png(beecn_url, neighborhood_url, plot_dir, show=False, figwidth=10, figheight=10, beecncolor='blue', neighborhoodcolor='green'):
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


def plot_beecn_html(neighborhood_geo, plot_dir, population_csv, fillcolor='YlGn', fillopacity=0.9, lineopacity=0.2):
    neighborhood_geo = neighborhood_geo
    population_df = pd.read_csv(population_csv)
    m = folium.Map(location=[45.5236, -122.6750])


    population = folium.Choropleth(
                                   geo_data=neighborhood_geo,
                                   data=population_df,
                                   columns=['OBJECTID', 'Total'],
                                   key_on='feature.properties.OBJECTID',
                                   fill_color=fillcolor,
                                   fill_opacity=fillopacity,
                                   line_opacity=lineopacity,
                                   legend_name='Neighborhood Population Size',
                                   highlight=True,
                                   name='2010 Population',
                                   show=True
    ).add_to(m)
    folium.GeoJson(
        neighborhood_geo,
        tooltip=folium.features.GeoJsonTooltip(fields=['NAME'],
                                               localize=True)
    ).add_to(population.geojson)
    m.save(os.path.join(plot_dir, 'beecn_map.html'))
    return
