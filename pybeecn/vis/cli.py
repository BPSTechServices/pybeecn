"""
This work was authored by Gabriel McBride in support
of Portland Open Data Program and Portland Bureau of
Emergency Management BEECN Program. The effort was
conducted as a use case for the student's masters
project to study the interaction between Systems
Engineering and Data Science activities.
"""

import argparse
from pybeecn.vis.mapping import view_map

def setup_beecn_parser(subp, parents):
    """
    BEECN Command Line Interface (CLI) Application
-------------------------------------------------------------
Purpose:
Provide a command line interface for viewing map boundary
data and points along with relevant population data.

Usage:
To run this command line utility download the associated
population data from

<https://github.com/glmcbr06/pybeecn/blob/master/
data/Census_2010_Data_Cleanedup_Neighborhoods2.csv>

Navigate to the page>Hold option or alt>click Raw

use this data to view a cloropleth of a variety of
demographic populations in Portland, OR by neighborhoods.

-------------------------------------------------------------
    :param subp:
    :param parents:
    :return:
    """
    # Create the parser
    parser = subp.add_parser('map', formatter_class=argparse.RawDescriptionHelpFormatter, description=setup_beecn_parser.__doc__, help='view the locations of BEECN sites', parents=parents)

    # Add arguments to the parser
    parser.add_argument('--show', default=False, action='store_true', help='show the plots during runtime')
    parser.add_argument('--directory', required=True, help='directory where to store the files generated from the analysis')
    parser.add_argument('--filePath', '-f', required=True, help='csv file with population data')
    parser.add_argument('--column', '-c', default='Total', type=str)
    parser.add_argument('--boundaries', required=True, help='Geographic boundaries for the map to plot')
    parser.add_argument('--points', required=True, help='The points to add to the map')
    parser.set_defaults(func=view_map)

def __argparse__(subp, parents=[]):
    """BEECN Application
    Put a description here
    :param subp:
    :param parents:
    :return:
    """

    setup_beecn_parser(subp, parents)

