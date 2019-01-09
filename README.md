# CloudComputing
## Description of the project
This is a GitHub Repo for our Application for the module COMSM0010 at the University of Bristol in 2018.

## Running web service
Have a look at http://textanalytics.lukaspman.io/ .
At the moment the project respectively the kubernetes cluster is hosted by Microsoft Azure.

[![Build Status](https://dev.azure.com/brsccproject/textanalytica/_apis/build/status/textanalytica-Docker%20container-CI?branchName=master)](https://dev.azure.com/brsccproject/textanalytica/_build/latest?definitionId=1?branchName=master)

## Deprecated README can be seen below

## Getting started

### Run it native

* Install python3 (version 3.6 or higher)
* Install python-virtualenv
* Install pip3 (python3-pip)
* Clone the repo and cd into the root folder (here you should see this README file)
* Create virtualenv: ___$py -m venv venv___
* activate virtualenv: ___$. /venv/bin/activate___ (the point in the beginning is important)
* Install needed modules: ___$pip3 install flask___ and ___$pip3 install flask_pymongo___
* start server: ___$python3 src/app.py___
* open browser and navigate to localhost:5000

**Note:** At the moment this is under developement and the instruction abough may change. So this are more or less just some notes.

### Using Docker

* Install docker and docker-composer (on mac additional boot2docker or similar tool)
* cd into src/ folder
* run docker-composer up
* open browser and navigate to localhost:5000
