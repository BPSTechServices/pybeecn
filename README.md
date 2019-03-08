# WIP - PyBEECN

# Table of Contents

1. [Overview](#overview)
  * [Purpose](#purpose)
2. [Installation](#installation)
  * [Installing python and PIP](#installing-python-and-pip)
3. [Collaboration](#collaboration)
4. [Usage](#usage)

## Overview

### Purpose

## Installation
Additional instructions on environment setup and dependencies are comming soon.

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
Find out what pybeecn has to offer by running the followng in the commandline after your environment is :
```bash
pybeecn -h
```
