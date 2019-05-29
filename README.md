# Serverless Calorie Calculator
Basic serverless demo API for calculating calories burned.

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
