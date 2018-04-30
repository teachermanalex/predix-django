# Running the app

Clone this repository and change directory to timeseries-microservice.

## Installing dependencies

Run ```pip install -r requirements.txt``` to install the application's dependencies.

## Running locally

Update the ```manifest.yml``` file with your services' metadata.

Run ```python manage.py runserver``` to start a local server.

## Pushing to the cloud

Run ```cf push``` to push the app to the cloud.


# Notes For the lab

In this exercise, students build a data handler application (microservice). The microservice should pull data from the connected cars simulator using its REST endpoints. The microservice should then ingest the data into the Time Series service instance using the Predix Time Series SDK.

The data handler microservice has uses the following dependencies:
* Python 3
* Django 1.11
* Django REST Framework 3.6.2
* Predix Python SDK

All of the application’s dependencies have been added to the requirements.txt file.

SIMULATOR REST endpoint

GET /cars/simulator
```
[
    {
        "currentTime": 1524773044421,
        "id": "CC1",
        "name": "Ford Fusion",
        "odometerReading": 154427,
        "outsideTemp": 91,
        "engineTemp": 207,
        "speed": 38,
        "fuelLevel": 95,
        "parkingBrakeStatus": 0,
        "gasCapStatus": 0,
        "windowStatus": 0
    },
    {
        "currentTime": 1524773044421,
        "id": "CC2",
        "name": "Hyundai Sonata",
        "odometerReading": 190946,
        "outsideTemp": 58,
        "engineTemp": 220,
        "speed": 82,
        "fuelLevel": 45,
        "parkingBrakeStatus": 0,
        "gasCapStatus": 0,
        "windowStatus": 0
    },
    {
        "currentTime": 1524773044421,
        "id": "CC3",
        "name": "Toyota Prius",
        "odometerReading": 251352,
        "outsideTemp": 52,
        "engineTemp": 192,
        "speed": 8,
        "fuelLevel": 9,
        "parkingBrakeStatus": 0,
        "gasCapStatus": 0,
        "windowStatus": 0
    },
    {
        "currentTime": 1524773044421,
        "id": "CC4",
        "name": "Mercedes-Benz CLA",
        "odometerReading": 132701,
        "outsideTemp": 111,
        "engineTemp": 211,
        "speed": 74,
        "fuelLevel": 97,
        "parkingBrakeStatus": 0,
        "gasCapStatus": 0,
        "windowStatus": 0
    },
    {
        "currentTime": 1524773044421,
        "id": "CC5",
        "name": "Chevrolet Camaro",
        "odometerReading": 169345,
        "outsideTemp": 73,
        "engineTemp": 218,
        "speed": 55,
        "fuelLevel": 83,
        "parkingBrakeStatus": 0,
        "gasCapStatus": 1,
        "windowStatus": 0
    }
]
```

**NOTE**

* Ignore this if you're not using the Virtual Machine.
* From your terminal, start your Virtual machine by running ```vagrant up```. Once the machine starts, log in to the machine by running ```vagrant ssh```
* Run ```cd /vagrant``` and make sure you're working in your virtual environment by running ```workon <your-virtualenv>```

* Change directory to the data handler application by running ```cd django-predix/django-data-handler```
* Install the app's dependencies by running ```pip install -r requirements.txt```
* You will be still be working on the host machine. We will be using the virtual machine only to run our applicaion.

**END NOTE**

Install the app's dependencies by running ```pip install -r requirements.txt```.

### Update the manifest file

Update the manifest file with your services' metadata. Enter your environment variables for
* UAA Issuer ID
* UAA Client ID
* UAA Client Secret
* Timeseries Ingest URI
* Timeseries Zone ID
* Connected Cars Simulator URL

Your manifest file should look like this

<p align="center">
  <img src="https://i.imgur.com/e9Hpymt.png" />
</p>

### Ingesting data

We're using the Predix Python SDK to ingest data into Timeseries. In the ```/predix_api/apps.py``` file is where we're defining the ingestion logic. The method ```getAndIngest``` is already defined to ingest each car's speed every 5 seconds. To ingest any other data point, for example, the engine temperature, add the following line after line 34.

```ts.send(data['id']+'_engineTemp', data['engineTemp'], quality=3, timestamp=data['currentTime'])```

This will create a new tag, in ```<Car_ID>_engineTemp``` format. For example, ```CC1_engineTemp``` and ingest data every 5 seconds.

### Runing the application locally

To run the application, run the following command (On your VM, if you are using one)

```python3 manage.py runserver 0:8080```

### Validate Time Series data

* Open the Predix Tool Kit  https://predix-toolkit.run.aws-usw02-pr.ice.predix.io/
* Select API Explorer.
* Login as Client (enter UAA URL, Client ID, Client Secret).
* Switch to Time Series Query.
* Choose Request:  OrderedDatapoints Request.
* Enter your time series zone ID.
* In the Request Body, change “start” to “1h-ago”.
* Enter a tag namesuch as CC1_speed

<p align="center">
  <img src="https://i.imgur.com/NXB2Oew.png" width="75%"/>
</p>

<p>
  <img src="https://i.imgur.com/LIrtouY.png" width="35%"/>
</p>

## Deploy the app

Login to cloudfoundry and select your org and space. Check your manifest and add the timeseries and uaa service labels and metadata to the file.

Run ```cf push``` to push the app to the cloud.
