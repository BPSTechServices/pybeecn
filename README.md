# PyBEECN

# Table of Contents

1. [Overview](#overview)
  * [Purpose](#purpose)
2. [Installation](#installation)
  * [Installing python and PIP](#installing-python-and-pip)
3. [Collaboration](#collaboration)
4. [Usage](#usage)

## Overview
This project will be developed using a Systems Engineering approach along with utilizing the standard git development practices within each lifecycle phase. Here are a few places to reference for git development. [GitHub Guide](https://guides.github.com/introduction/flow/), [Stackoverflow](https://stackoverflow.com/questions/19695127/git-workflow-review), and [Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows)

### Purpose
This effort will be focused on helping [Portland Bureau of Emergency Management](https://www.portlandoregon.gov/pbem/) and [Portland's Open Data Program](https://www.portlandoregon.gov/bps/76768) make decisions regarding the [BEECN](https://www.portlandoregon.gov/pbem/59630) Program. The effort may also provide insight that may prove useful for a number of other city efforts such as, the [NET](https://www.portlandoregon.gov/pbem/31667) Program. Our primary objective is to understand the behavior of the population and other characteristics of each neighborhood as well as the different demographics within the neighborhoods and how these populations will be affected given a major earthquake in the area. 

## Installation
Additional instructions on environment setup and dependencies are coming soon.

### Installing python and PIP
If you do not have a python environment setup on your machine, please follow the instructions [here](https://penandpants.com/2012/02/24/install-python/). The page also provides a good description of the tools that will be used in the environment. Other general instructions for installing packages using PIP can be found [here](https://packaging.python.org/tutorials/installing-packages/).

Additionally, an alternative to using PIP for managing a python environment is [ANACONDA FOR PYTHON](https://www.anaconda.com/what-is-anaconda/). However, I am recommending against using anaconda for this project unless you are familiar or comfortable using it. 

## Collaboration
If you would like to contribute to the effort to improve Portland's BEECN program through the use of available data please contact Gabe McBride at [gabe.l.mcbride@gmail.com](mailto:gabe.l.mcbride@gmail.com).

### Development
If you would like to contribute as a developer of the pybeecn module, please contact the email above and setup a working directory. Suggested directory structure:

* Home directory
  * data (a place to keep relevant data to the project)
  
  * projects (This will be where you clone the pybeecn repository)
  
When you have the folder structure that you want run the following in the commad line:
```bash
cd ~/your_folder/your_folder
git clone https://github.com/glmcbr06/pybeecn.git
cd pybeecn
pip install --upgrade --no-deps -e .
```
  

## Usage
Find out what pybeecn has to offer by running the followng in the command line after your environment is :
```bash
pybeecn -h
```
### Jupyter Notebook
Insert instructions on how to use the Jupyter Notebook file here.

## References
https://www.portlandoregon.gov/civic/56897

folium tooltip helpful advice: https://github.com/python-visualization/folium/issues/469