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


def plot_population_map_html(boundary_url, points_url, plot_dir,  population_csv, population_column='Total', fill_color='YlGn', fill_opacity=0.6, line_opacity=0.2):

    population_df = pd.read_csv(population_csv)
    m = folium.Map(location=[45.5236, -122.6750], zoom_start=11.5)

    population = folium.Choropleth(
                                   geo_data=boundary_url,
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
        boundary_url,
        tooltip=folium.features.GeoJsonTooltip(fields=['NAME'],
                                               localize=True,
                                               sticky=True),
        smooth_factor=0.01
    ).add_to(population.geojson)

    points_gpd = gpd.read_file(points_url)
    points_df = pd.DataFrame(points_gpd)

    points_df['geometry'] = points_df['geometry'].map(lambda x: str(x).lstrip('POINT (').rstrip(')'))
    lat = []
    lon = []

    for row in points_df['geometry']:
        try:
            lon.append(row.split(' ')[0])
            lat.append(row.split(' ')[1])
        except:
            lon.append(np.NaN)
            lat.append(np.NaN)

    points_df['latitude'] = lat
    points_df['longitude'] = lon

    latitude = np.array(points_df['latitude'])
    latitude = latitude.astype(float)
    longitude = np.array(points_df['longitude'])
    longitude = longitude.astype(float)
    # todo: Figure out more generic way to do this so other data can come in
    #  or make a separate function to add the tool tip.
    beecn_site = points_df['SITE_NAME']
    address = points_df['LOCATION']

    location = zip(latitude, longitude)

    points_fg = folium.FeatureGroup(name='BEECN Locations')
    ring_fg = folium.FeatureGroup(name='1600m Radius')
    count = 0
    for i in location:
        tooltip = '<b>Name</b>: {} <br> ' \
                  '<b>Address</b>: {} <br>' .format(beecn_site[count], address[count])
        folium.Marker(i, icon=folium.Icon(icon='medkit', prefix='fa'),
                      tooltip=tooltip).add_to(points_fg)
        folium.Circle(i,
                      weight=1.5,
                      radius=1600).add_to(ring_fg)
        count += 1

    points_fg.add_to(m)
    ring_fg.add_to(m)
    m.add_child(folium.LayerControl())

    map_path = os.path.join(plot_dir, '{}_population_map.html'.format(population_column))
    logger.info('saving {}'.format(map_path))
    m.save(map_path)

    return m


