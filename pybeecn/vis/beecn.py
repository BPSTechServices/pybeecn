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
import numpy as np
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


def beecn_lat_long(beecn_geo):
    beecn_geo = gpd.read_file(beecn_geo)
    beecn_df = pd.DataFrame(beecn_geo)

    beecn_df['geometry'] = beecn_df['geometry'].map(lambda x: str(x).lstrip('POINT (').rstrip(')'))
    lat = []
    lon = []

    for row in beecn_df['geometry']:
        try:
            lon.append(row.split(' ')[0])
            lat.append(row.split(' ')[1])
        except:
            lon.append(np.NaN)
            lat.append(np.NaN)

    beecn_df['latitude'] = lat
    beecn_df['longitude'] = lon
    return beecn_df


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


def plot_beecn_html(neighborhood_geo, plot_dir, beecn_geo, population_csv, population_column='Total', fill_color='YlGn', fill_opacity=0.6, line_opacity=0.2):
    neighborhood_geo = neighborhood_geo
    population_df = pd.read_csv(population_csv)
    m = folium.Map(location=[45.5236, -122.6750], zoom_start=11.5)

    population = folium.Choropleth(
                                   geo_data=neighborhood_geo,
                                   data=population_df,
                                   columns=['OBJECTID', population_column],
                                   key_on='feature.properties.OBJECTID',
                                   fill_color=fill_color,
                                   fill_opacity=fill_opacity,
                                   line_opacity=line_opacity,
                                   legend_name='Neighborhood {} Population Size'.format(population_column),
                                   highlight=True,
                                   name='2010 {} Population'.format(population_column),
                                   show=True
    ).add_to(m)
    folium.GeoJson(
        neighborhood_geo,
        tooltip=folium.features.GeoJsonTooltip(fields=['NAME'],
                                               localize=True,
                                               sticky=True),
        smooth_factor=0.01
    ).add_to(population.geojson)

    beecn_geo = gpd.read_file(beecn_geo)
    beecn_df = pd.DataFrame(beecn_geo)

    beecn_df['geometry'] = beecn_geo['geometry'].map(lambda x: str(x).lstrip('POINT (').rstrip(')'))
    lat = []
    lon = []

    for row in beecn_df['geometry']:
        try:
            lon.append(row.split(' ')[0])
            lat.append(row.split(' ')[1])
        except:
            lon.append(np.NaN)
            lat.append(np.NaN)

    beecn_df['latitude'] = lat
    beecn_df['longitude'] = lon

    latitude = np.array(beecn_df['latitude'])
    latitude = latitude.astype(float)
    longitude = np.array(beecn_df['longitude'])
    longitude = longitude.astype(float)
    beecn_site = beecn_geo['SITE_NAME']
    address = beecn_geo['LOCATION']

    location = zip(latitude, longitude)

    beecn_fg = folium.FeatureGroup(name='BEECN Locations')
    ring_fg = folium.FeatureGroup(name='1600m Radius')
    count = 0
    for i in location:
        tooltip = '<b>Name</b>: {} <br> ' \
                  '<b>Address</b>: {} <br>' .format(beecn_site[count], address[count])
        folium.Marker(i, icon=folium.Icon(icon='medkit', prefix='fa'),
                      tooltip=tooltip).add_to(beecn_fg)
        folium.Circle(i,
                      weight=1.5,
                      radius=1600).add_to(ring_fg)
        count += 1

    beecn_fg.add_to(m)
    ring_fg.add_to(m)
    m.add_child(folium.LayerControl())

    map_path = os.path.join(plot_dir, '{}_population_map.html'.format(population_column))
    logger.info('saving {}'.format(map_path))
    m.save(map_path)

    return m


