# Technical Case

This project gives you the configuration to start working on the technical case.

## Start the API

To start the django api, you have a docker-compose file. You must have docker and docker-compose installed on your computer.

1. Build the containers
```bash
docker-compose build
```
2. launch the project
```bash
docker-compose up -d
```
3. visit localhost:8000 and check that django is working


## Run the migrations

Once the API is up and running, you can start developing on it.
First you will need to run the first django migrations.
1. Open a console on the container that is running the API.
```bash
docker-compose exec api /bin/bash
```
2. Run the migrations
```bash
python manage.py migrate
```

## Develop your own code

Now that you have everything ready, you can start editing the files of this project. As there is a mapping between the local volume and the container volume, anything you will edit locally will be edit in the container. You can use the console as you did on the previos step to make migrations, run migrations or install requirements and the API will continue running. If you did something wrong with the API, you can restart the container runnning the API with the command:
```bash
docker-compose restart api
```

## Routes

# Accounts
```bash
api/v1/accounts/register/
api/v1/accounts/login/
api/v1/accounts/logout/
```

# Plots
```bash
api/v1/plots/create/
api/v1/plots/<int:pk>/
api/v1/plots/<int:pk>/delete/
api/v1/user-plots/
```

# Example of data to send for the creation of a plot
```bash
{

  "name": "parcelle 1",
  "zone": [
      {
        "lat": 48.68347772580688,
        "lng": 4.139563432670286
      },
      {
        "lat": 48.68385980862524,
        "lng": 4.1425397283311725
      },
      {
        "lat": 48.67647236043237,
        "lng": 4.14237437857247
      },
      {
        "lat": 48.67663613334162,
        "lng": 4.1394807577909205
      },
      {
        "lat": 48.68347772580688,
        "lng": 4.139563432670286
      }
  ]
}
```
