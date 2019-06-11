"""
This work was authored by Gabriel McBride in support 
of Portland Open Data Program and Portland Bureau of 
Emergency Management BEECN Program. The effort was 
conducted as a use case for the student's masters 
project to study the interaction between Systems 
Engineering and Data Science activities. 
"""
import os
import shutil
import logging.config
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
from folium import IFrame
import numpy as np
logger = logging.getLogger(__name__)



# Make Visualization Functions
# ----------------------------------------------------------------------------------------------------------------------
def plot_boundary_points_png(point_gpd: gpd.geodataframe, boundary_gpd: gpd.geodataframe, plot_dir, show=False, figwidth=10, figheight=10, point_color='blue', boundary_color='green'):

    f, ax = plt.subplots(figsize=(figwidth, figheight))
    boundary_gpd.plot(ax=ax, color=boundary_color)
    point_gpd.plot(ax=ax, color=point_color)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('BEECN Locations in Portland, OR')
    if show:
        plt.show()
    f.savefig(os.path.join(plot_dir, 'beecn_locations.png'))
    return


def setup_analysis_directory(directory):
    directory = os.path.abspath(directory)
    dirs = dict(
        plots=os.path.join(directory, 'plot_files'),
        data=os.path.join(directory, 'data_files'),
        alerts=os.path.join(directory, 'alert_files'),
        report=os.path.join(directory, 'final_report')
    )

    # Creating New Analysis Directory (if required)
    if not os.path.exists(directory):
        logger.info("Creating New Analysis Directory: {}".format(directory))
        os.makedirs(directory)

    # Creating Sub directories
    for name, d in dirs.items():
        if not os.path.exists(d):
            logger.info("Creating Analysis {} Directory: {}".format(name, d))
            os.makedirs(d)

    return dirs


def plot_population_map_html(boundary_url, points_url, plot_dir, population_column='Total_Pop_5_n_over', fill_color='YlGn', fill_opacity=0.6, line_opacity=0.2):
    points_gpd = gpd.read_file(points_url)
    points_df = pd.DataFrame(points_gpd)
    population_df = gpd.read_file(boundary_url)
    pop_list = ['OBJECTID', 'Total_Pop_5_n_over', 'Spanish', 'Russian', 'Other_Slavic', 'Other_Indic',
                'Other_Indo_European', 'Chinese', 'Japanese', 'Korean', 'Mon_Khmer_Cambodian', 'Laotian', 'Vietnamese',
                'Other_Asian', 'Tagalog', 'Other_Pacific_Island', 'Arabic', 'African']

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

    m = folium.Map(location=[latitude.mean(), longitude.mean()], zoom_start=11.5)
    population = folium.Choropleth(
                                   geo_data=boundary_url,
                                   data=population_df,
                                   columns=['OBJECTID', population_column],
                                   key_on='feature.properties.OBJECTID',
                                   fill_color=fill_color,
                                   fill_opacity=fill_opacity,
                                   line_opacity=line_opacity,
                                   legend_name='{} Population Size by Tract'.format(population_column),
                                   highlight=True,
                                   name='Date {} Population'.format(population_column),
                                   show=True
    ).add_to(m)
    folium.GeoJson(
        boundary_url,
        tooltip=folium.features.GeoJsonTooltip(fields=pop_list,
                                               localize=True,
                                               sticky=True),
        smooth_factor=0.01
    ).add_to(population.geojson)

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
                  '<b>Address</b>: {} <br>'.format(beecn_site[count], address[count])
        folium.Marker(i, icon=folium.Icon(icon='medkit', prefix='fa'),
                      tooltip=tooltip).add_to(points_fg)
        folium.Circle(i,
                      weight=1.5,
                      radius=1600).add_to(ring_fg)
        count += 1

    points_fg.add_to(m)
    ring_fg.add_to(m)
    m.add_child(folium.LayerControl())

    # text = 'Here is some test text'
    # iframe = IFrame(text, width=700, height=450)
    # popup = folium.Popup(iframe, max_width=3000)
    #
    # Text = folium.Marker(location=[latitude.max(), longitude.max()], popup=popup,
    #                      icon=folium.Icon(icon_color='black'), draggable=True)
    #
    # m.add_child(Text)

    map_path = os.path.join(plot_dir, '{}_population_map.html'.format(population_column))
    m.save(map_path)

    return m

# Make data functions
# ----------------------------------------------------------------------------------------------------------------------


def geo_json_to_df(geo_url: str):
    data = gpd.read_file(geo_url)
    return data


def get_id_and_pop(data: pd.DataFrame):
    pop_list = ['OBJECTID', 'TRACT', 'Total_Pop_5_n_over', 'Spanish', 'Russian', 'Other_Slavic', 'Other_Indic',
                'Other_Indo_European', 'Chinese', 'Japanese', 'Korean', 'Mon_Khmer_Cambodian', 'Laotian', 'Vietnamese',
                'Other_Asian', 'Tagalog', 'Other_Pacific_Island', 'Arabic', 'African']
    data = pd.DataFrame(data, columns=pop_list)
    return data


def make_totals_df(data: pd.DataFrame):

    pop_dict = {}
    for col in data:
        if not col == 'OBJECTID' and not col == 'TRACT':
            pop_dict[col] = data[col].sum()
    df = pd.DataFrame.from_dict(pop_dict, orient='index', columns=['population'])
    # total_total = df.loc[df.index == 'Total_Pop_5_n_over'].iloc[0]
    # pops_total = df.loc[df.index != 'Total_Pop_5_n_over'].iloc[0:len(df)]
    # pops_sum = pops_total.population.sum()
    # df.loc['other_over_5'] = total_total - pops_sum
    df.index.names = ['demographic']
    return df


def make_tract_pops_df(df):
    print(df)


def make_population_bar(data: pd.DataFrame, ax=None):
    data.plot.barh(ax=ax)


def get_single_population(data_gpd, column):
    single_pop_df = pd.DataFrame(data_gpd[[column, 'OBJECTID', 'NAME']])
    # single_pop_df.loc['Total'] = single_pop_df['Total_Pop_5_n_over'].sum()
    # Could make another percentage column here if necessary
    return single_pop_df

