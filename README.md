# Serverless Calorie Calculator [![CircleCI](https://circleci.com/gh/cbusseata/serverless-calorie-calculator/tree/master.svg?style=svg)](https://circleci.com/gh/cbusseata/serverless-calorie-calculator/tree/master)
Basic serverless demo API for calculating calories burned.

This repository is integrated with Circle CI and any commit to the master branch that passes unit tests is deployed to 
a staging environment in AWS, and if the automated acceptance tests pass, it is deployed to an AWS production environment.

## Dev Environment

### Preqrequisites:
* docker
* docker-compose

### Using the dev environment:
To start the dev environment, execute the following command from the root of this repo:
````bash
make
````

This will start a single 'app' container, and the API will be available at http://0.0.0.0:3000.

To test the API, you must include an x-api-key header ('local-test' for local development).  You can use the
Postman collection found in the docs directory of this repository.

## Adding/removing modules
Use pipenv from inside the app container
````bash
$ make enter

  Enter the name of the service that you want to access, choices are:
  app
  Service name: app

bash-4.2# pipenv install <module>
````

## Tests

### Unit Tests
This repository uses pytest for unit testing.  To execute unit tests, from within the app container:
````bash
pytest tests/unit
````

### Acceptance Tests
This repository uses the robot framework for automated API acceptance testing.  To execute the robot tests,
from within the app container:
````bash
tests/acceptance/runtests.sh <environment>
````
Replace <environment> with 'local' for testing locally.

## Next Steps

* API documentation - The serverless-aws-documentation plugin is currently used to add documentation to API Gateway in AWS.
The next step is to, during a deploy, download the swagger json file from API Gateway, generate a nice HTML file, and upload
that to S3 as a publicly available static web page, and add a link to it from this document.
* Add support for more activities