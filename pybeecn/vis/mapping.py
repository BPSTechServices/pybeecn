import os
import shutil
import logging.config
from . import beecn as bn
import geopandas as gpd
import matplotlib.pyplot as plt
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
    pop_list = ['Total_Pop_5_n_over', 'Spanish', 'Russian', 'Other_Slavic', 'Other_Indic',
                'Other_Indo_European', 'Chinese', 'Japanese', 'Korean', 'Mon_Khmer_Cambodian',
                'Laotian', 'Vietnamese', 'Other_Asian', 'Tagalog', 'Other_Pacific_Island',
                'Arabic', 'African']

    # Setup plot directory
    # -----------------------------------------------------------------------------------------------------------------
    directory = os.path.join(args.directory, 'beecn')

    # Setup the directory
    # -----------------------------------------------------------------------------------------------------------------
    dirs = bn.setup_analysis_directory(directory)
    # These should be imported as args.urls or something
    # -----------------------------------------------------------------------------------------------------------------
    point_url = args.points
    boundary_url = args.boundaries
    beecn_gpd = gpd.read_file(point_url)  # args urls should go here.
    tract_gpd = gpd.read_file(boundary_url)

    # plot_boundary_points_png(point_gpd=beecn_gpd, boundary_gpd=tract_gpd, plot_dir=dirs['plots'])

    # Get the total Population data to plot
    # -----------------------------------------------------------------------------------------------------------------
    pop_df = bn.get_single_population(tract_gpd, column='Total_Pop_5_n_over')

    bn.plot_population_map_html(boundary_url=boundary_url, points_url=point_url, plot_dir=dirs['plots'])

    # Make some data frames
    # -----------------------------------------------------------------------------------------------------------------
    geo_df = bn.geo_json_to_df(geo_url=boundary_url)
    pops_id_tract_df = bn.get_id_and_pop(geo_df)
    pops_df = bn.make_totals_df(pops_id_tract_df)
    fname = os.path.join(dirs['data'], 'portland_total_populations.csv')
    pops_df.to_csv(fname)
    # Plot the populations
    # -----------------------------------------------------------------------------------------------------------------
    # f, ax = plt.subplot(nrows=1, ncols=1, figsize=(20, 20))

    f, ax = plt.subplots(figsize=(10, 10))
    bn.make_population_bar(pops_df[pops_df.index != 'Total_Pop_5_n_over'], ax=ax)
    plt.title('Limited English Speaking Populations')
    plt.tight_layout(pad=1.1)
    fname = os.path.join(dirs['plots'], 'total_population_bar.png')
    f.savefig(fname)

    # Make population dfs
    # -----------------------------------------------------------------------------------------------------------------

