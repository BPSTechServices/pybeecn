import argparse
from . import view as vw

def setup_beecn_parser(subp, parents):
    """BEECN Command Line Interface (CLI) Application
-------------------------------------------------------------
Add description of the BEECN CLI tool and commands here

-------------------------------------------------------------
    """
    # Create the parser
    parser = subp.add_parser('locations', formatter_class=argparse.RawDescriptionHelpFormatter, description=setup_beecn_parser.__doc__, help='view the locations of BEECN sites', parents=parents)

    # Add arguments to the parser
    parser.add_argument('--show', default=False, action='store_true', help='show the plots during runtime')
    parser.add_argument('--directory', required=True, help='directory where to store the files generated from the analysis')
    parser.add_argument('--filePath','-f', required=True, help='csv file with population data')
    parser.set_defaults(func=vw.view)

def __argparse__(subp, parents=[]):
    """BEECN Application
    Put a description here
    :param subp:
    :param parents:
    :return:
    """


    setup_beecn_parser(subp, parents)

