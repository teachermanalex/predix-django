# Notes for the Lab

In this exercise, students build a UI application (microservice). The microservice should pull data from the Predix services and display on the dashboard. 

The UI microservice has uses the following technologies:
* Predix Polymer Webcomponents
* Django 1.11
* Django REST Framework 3.6.2
* Predix Python SDK

All of the application’s dependencies have been added to the requirements.txt file.

**NOTE**
* Ignore this if you're not using the Virtual Machine.
* From your terminal, start your Virtual machine by running ```vagrant up```. Once the machine starts, log in to the machine by running ```vagrant ssh```
* Run ```cd /vagrant``` and make sure you're working in your virtual environment by running ```workon <your-virtualenv>```
* Change directory to the data handler application by running ```cd django-predix/django-ui```
* Install the app's dependencies by running ```pip install -r requirements.txt```
* You will be still be working on the host machine. We will be using the virtual machine only to run our applicaion.

**END NOTE**

## Install Dependencies
Install the app's dependencies by running the following commands

```pip3 install -r requirements.txt```

```bower install```

## Update the manifest file

Update the manifest file with your services' metadata. Enter your environment variables for
* UAA Issuer ID
* UAA Client ID
* UAA Client Secret
* Timeseries Ingest URI
* Timeseries Zone ID
* Asset URI
* Asset Zone ID

## Running the app locally

To run the application, run the following command (On your VM, if you are using one)

```python3 manage.py runserver 0:8080```

## Deploy the app

Login to cloudfoundry and select your org and space. Check your manifest and add the timeseries and uaa service labels and metadata to the file.

Run ```cf push``` to push the app to the cloud.
