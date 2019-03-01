import logging
import argparse
import os
from . import view as vw

def setup_beecn_parser(parser, parents=[]):
    """BEECN Command Line Interface (CLI) Application
-------------------------------------------------------------
Add description of the BEECN CLI tool and commands here

-------------------------------------------------------------
    """
    test_parser = argparse.ArgumentParser(add_help=False)
    test_parser.add_argument('--test', '-T', default=None, help='Testing a parser')

    subp = parser.add_subparsers()
    parser = subp.add_parser('file', formatter_class=argparse.RawDescriptionHelpFormatter,
                             description=vw.view.__doc__, help='Subcommand test', parents=parents)
    parser.set_defaults(func=vw.view)

def run(args):
    print('This is the run args function')

def __argparse__(subp, parents=[]):
    """BEECN Application
    Put a description here
    :param subp:
    :param parents:
    :return:
    """
    parser = subp.add_parser('test',
                             formatter_class=argparse.RawDescriptionHelpFormatter,
                             description=vw.view.__doc__,
                             help='test for beecn commands',
                             parents=parents)
    setup_beecn_parser(parser, parents)

