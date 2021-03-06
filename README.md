# Ride-My-Way

[![Coverage Status](https://coveralls.io/repos/github/wandesky/lets-ride/badge.svg)](https://coveralls.io/github/wandesky/lets-ride)
[![Build Status](https://travis-ci.org/wandesky/lets-ride.svg?branch=develop)](https://travis-ci.org/wandesky/lets-ride)
[![Maintainability](https://api.codeclimate.com/v1/badges/cc2ab8ceaf068ba0bccd/maintainability)](https://codeclimate.com/github/wandesky/lets-ride/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/cc2ab8ceaf068ba0bccd/test_coverage)](https://codeclimate.com/github/wandesky/lets-ride/test_coverage)

Repository for Andela Kenya Cohort 29 Bootcamp Developer Challenge.

Ride My Way is a carpooling web application.
The app gives drivers a platform where they can create ride offers and a place where passangers can access available ride offers.

# Author:
    Brian Wandera (@wandesky)

# What to expect during (Challenge 2)
    This repo will host the work done while undertaking Challenge 2 of Andela Bootcamp 29
    On successful completion of this track, the following features should be working
    - A user should be able to access all available rides
    - A user should be able to access details for a specific ride
    - A driver should be able to create a new ride offer
    - A passenger should be able to make a request to join a ride

# Installation guide
## Want to have a look at the work done so far

    There are two ways you can preview the current state of this work
### Using localhost
Include steps to run the code on localhost
### Using Heroku 
Include steps to run the code on heroku 
https://lets-ride-heroku-staging.herokuapp.com/api/v1/rides


## The API
The features in challenge 2 are implemented using API's. The table below shows the API endpoints to be followed.
### Endpoints

| EndPoint | Functionality |
| ------------- | ------------- |
| GET /rides | Fetch all ride offers  |
| GET /rides/<rideId> | Fetch a single ride offer  |
| POST /rides | Create a ride offer |
| POST /rides/< rideId >/requests | Make a request to join a ride |
|  |  |
