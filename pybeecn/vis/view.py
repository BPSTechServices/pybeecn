import matplotlib.pyplot as plt
import geopandas
import os

# Todo: folium not working in cli program. Works in jupyter notebook environment.
#  Get working with cli for ability to save html files. May also lead to being able to use html in markdown file.
# folium not working in cli program.
# import folium
# import branca
import pandas as pd


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
        os.makedirs(data_dir)

    plot_dir = os.path.join(args.directory, 'plot_files')
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)


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

    # Todo: get code below to run with folium working to save html map.
    # neigh_geo = 'https://opendata.arcgis.com/datasets/9f50a605cf4945259b983fa35c993fe9_125.geojson'
    # data_dir = os.path.join(os.path.dirname(os.getcwd()), 'data')
    #
    # neighbor_file = os.path.join(data_dir, 'neighborhood_population.csv')
    #
    # # Way Jupyter Notebook and local machine read in files is different. Use this
    # if os.path.exists(neighbor_file):
    #     neighbor_df = pd.read_csv(neighbor_file)
    # else:
    #     data_dir = os.path.join(os.getcwd(), 'pybeecn/data')
    #     neighbor_file = os.path.join(data_dir, 'neighborhood_population.csv')
    #     neighbor_df = pd.read_csv(neighbor_file)
    #
    # print(neighbor_df.head())
    #
    # m = folium.Map(location=[45.5236, -122.6750])
    # folium.Choropleth(geo_data=neigh_geo,
    #                   name='2010 Population',
    #                   data=neighbor_df,
    #                   columns=['OBJECTID', 'POPULATION'],
    #                   key_on='feature.properties.OBJECTID',
    #                   fill_color='YlGn',
    #                   fill_opacity=0.7,
    #                   line_opacity=0.2,
    #                   legend_name='Neighborhood Population Size',
    #                   ).add_to(m)
    # folium.LayerControl().add_to(m)
    # m.save(plot_dir, 'map.html')
