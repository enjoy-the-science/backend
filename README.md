# Annotator Platform Backend  
## Overview  
This is the backend for the annotator platform. It provides API endpoints
for the platform and acts as an authorization provider for the Orthanc DICOM server.  
## Setup
To build and start the backend separately, use the included **docker-compose** config:  
```bash
docker-compose up
```  
Access the API via the `8080` port.  
Access Orthanc via the `8042` port.  
**Make sure both ports are available before starting the services!**  
## Dependencies  
Dependencies of the project are managed by [Poetry](https://github.com/python-poetry/poetry).
To install it, use  
```bash
pip install poetry
```
To create a new virtual environment and install the dependencies from the `poetry.lock`, use
```bash
poetry install
```
in the project root folder. 

This will install both production and dev dependencies. If, for some reason, you do not require
dev dependencies, use the command above with the `--no-dev` flag.
