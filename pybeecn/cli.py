import pkg_resources
import logging
import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def pass_message(msg):
    return '{}'.format(msg)+'.'*5+'{}PASSED'.format(bcolors.OKGREEN, bcolors.ENDC)

def fail_message(msg):
    return "{}".format(msg)+"."*5+"{}FAILED{}".format(bcolors.FAIL,bcolors.ENDC)


def warn_message(msg):
    return "{}".format(msg)+"."*5+"{}WARNING{}".format(bcolors.WARNING, bcolors.ENDC)

def error_message(msg):
    return "{}".format(msg)+"."*5+"{}{}ERROR{}".format(bcolors.UNDERLINE, bcolors.FAIL,bcolors.ENDC)

def run():
    """
    BEECN Command Line Interface (CLI) Application
-------------------------------------------------------------
Add description of the BEECN CLI tool and commands here

-------------------------------------------------------------
    :return:
    """
    epilog='\n For more information, please visit https://github.com/glmcbr06/pybeecn\n'
    epilog += ' or contact Gabriel McBride <gabe.l.mcbride@gmail.com>'

    mainparser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                         description=run.__doc__,
                                         epilog=epilog)

    module_parsers = mainparser.add_subparsers()

    verbose_parser = argparse.ArgumentParser(add_help=False)
    verbose_parser.add_argument('-v', '--verbose', action='count', default=0)

    for ep in pkg_resources.iter_entry_points(group='pybeecn.subcommands'):
        # Look into module for __argparse_ method and load it.
        try:
            logging.info('Attempting to load: {}'.format(ep))
            module = ep.load()
        except ImportError as e:
            logging.error('Failed to load subcommand {} due to failed import: {}'.format(ep, e))
        except Exception as e:
            logging.warn('Got exception: {} when trying to load module...passing'.format(e))
            pass
        else:
            if '__argparse__' in dir(module) and callable(module.__argparse__):
                docs = module.__argparse__.__doc__
                mparser = module_parsers.add_parser(ep.name,
                                                    help='This is a test help',
                                                    description=docs,
                                                    formatter_class=argparse.RawDescriptionHelpFormatter)
                module.__argparse__(mparser.add_subparsers(), [verbose_parser])

    args = mainparser.parse_args()
    if args.verbose > 0:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s--%(name)s:%(levelname)s:--%(message)s')
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s--%(name)s:%(levelname)s:--%(message)s')
        logging.getLogger().setLevel(logging.INFO)

    args.func(args)