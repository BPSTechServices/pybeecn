import logging
import argparse
import os
from . import view as vw

def setup_beecn_parser(subp, parents):
    """BEECN Command Line Interface (CLI) Application
-------------------------------------------------------------
Add description of the BEECN CLI tool and commands here

-------------------------------------------------------------
    """
    parser = subp.add_parser('test', formatter_class=argparse.RawDescriptionHelpFormatter, description=setup_beecn_parser.__doc__, help='this is a test', parents=parents)
    parser.add_argument('file', help='the file to view')
    parser.set_defaults(func=vw.view)

# def run(args):
#     print('This is the run args function')

def __argparse__(subp, parents=[]):
    """BEECN Application
    Put a description here
    :param subp:
    :param parents:
    :return:
    """
    # parser = subp.add_parser('test', formatter_class=argparse.RawDescriptionHelpFormatter,description=setup_beecn_parser.__doc__, help='test for beecn commands', parents=parents)


    setup_beecn_parser(subp, parents)

