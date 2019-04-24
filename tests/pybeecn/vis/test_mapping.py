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
import subprocess
import glob
from pybeecn.vis.mapping import view_map

# todo make a test for the top level function


def test_view():
    points_url = 'https://opendata.arcgis.com/datasets/6e6185533d5447deb8b7204c27e1858e_92.geojson'
    boundary_url = 'https://opendata.arcgis.com/datasets/9f50a605cf4945259b983fa35c993fe9_125.geojson'
    population_file = os.path.join(os.path.dirname(__file__), 'vis_data/Census_2010_Data_Cleanedup_Neighborhoods2.csv')
    print(population_file)
    tmp_dir = os.path.join('/tmp', 'test_beecn_files')
    plot_dir = os.path.join(tmp_dir, 'plots_dir')
    os.makedirs(tmp_dir)
    cmd = 'pybeecn vis map --directory {} '.format(tmp_dir)
    cmd += '--boundaries {} --points {} --filePath {}'.format(boundary_url, points_url, population_file)
    subprocess.check_output(cmd, shell=True)

    html_files = glob.glob(os.path.join(plot_dir, '*html*'))
    png_files = glob.glob(os.path.join(plot_dir, '*png*'))

    for f in html_files:
        assert os.path.getsize(f) > 0
    for f in png_files:
        assert os.path.getsize(f) > 0
    shutil.rmtree(tmp_dir)

