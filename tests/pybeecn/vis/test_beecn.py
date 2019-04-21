"""
This work was authored by Gabriel McBride in support 
of Portland Open Data Program and Portland Bureau of 
Emergency Management BEECN Program. The effort was 
conducted as a use case for the student's masters 
project to study the interaction between Systems 
Engineering and Data Science activities. 
"""

import os
import pybeecn.vis.beecn as bn
import shutil


def test_create_beecn_dir():
    directory = os.path.join('/tmp', 'test_beecn_files')
    bn.create_beecn_dir(directory)
    assert os.path.exists(directory)
    shutil.rmtree(directory)
    print('{} exists'.format(directory))