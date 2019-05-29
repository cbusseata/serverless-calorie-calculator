*** Settings ***
Documentation  Robot script for testing the calorie calculator API.
Variables  variables.py  ${ENVIRONMENT}
Library  REST  ${api base url}

*** Test Cases ***
Test no API key returns a 403 status code
    GET     /calculate/run?distance=2.1&hours=0&minutes=14&seconds=30&bodyweight=185&units=imperial
    Integer  response status    403

Test invalid API key returns a 403 status code
    Set Headers  {"x-api-key": "pineapple"}
    GET     /calculate/run?distance=2.1&hours=0&minutes=14&seconds=30&bodyweight=185&units=imperial
    Integer  response status    403
    
Test unsupported activity
    [Documentation]  Attempting to calculate calories for an unsupported activity.
    Expect Response  ${CURDIR}/schemas/response/errorResponse.json
    Set Headers  {"x-api-key": "${api key}"}
    GET     /calculate/cycle?distance=2.1&hours=0&minutes=14&seconds=30&bodyweight=185&units=imperial
    Integer  response status                   400
    Object   response body
    String   response body status              ERROR
    Object   response body errors
    Array    response body errors activity
    String   response body errors activity 0   I don't know what nonsense you're doing, but we only support 'walk' and 'run'

Test invalid units
    [Documentation]  Attempting to calculate calories for an invalid system of measurement.
    Expect Response  ${CURDIR}/schemas/response/errorResponse.json
    Set Headers  {"x-api-key": "${api key}"}
    GET      /calculate/run?distance=2.1&hours=0&minutes=14&seconds=30&bodyweight=185&units=english
    Integer  response status                400
    Object   response body
    String   response body status           ERROR
    Object   response body errors
    Array    response body errors units
    String   response body errors units 0   Invalid value, must be one of: imperial, metric.

Test bodyweight too low
    [Documentation]  Attempting to calculate calories for an invalid system of measurement.
    Expect Response  ${CURDIR}/schemas/response/errorResponse.json
    Set Headers  {"x-api-key": "${api key}"}
    GET      /calculate/run?distance=2.1&hours=0&minutes=14&seconds=30&bodyweight=0.001&units=imperial
    Integer  response status                     400
    Object   response body
    String   response body status                ERROR
    Object   response body errors
    Array    response body errors bodyweight
    String   response body errors bodyweight 0   Bodyweight must be at least 0.01

Test distance too short
    [Documentation]  Attempting to calculate calories for an invalid system of measurement.
    Expect Response  ${CURDIR}/schemas/response/errorResponse.json
    Set Headers  {"x-api-key": "${api key}"}
    GET      /calculate/run?distance=0.001&hours=0&minutes=14&seconds=30&bodyweight=185&units=imperial
    Integer  response status                   400
    Object   response body
    String   response body status              ERROR
    Object   response body errors
    Array    response body errors distance
    String   response body errors distance 0   Come on, distance must be at least 0.01!

Test valid request
    [Documentation]  Attempting to calculate calories for an invalid system of measurement.
    Expect Response  ${CURDIR}/schemas/response/successResponse.json
    Set Headers  {"x-api-key": "${api key}"}
    GET      /calculate/run?distance=2.1&hours=0&minutes=14&seconds=30&bodyweight=185&units=imperial
    Integer  response status            200
    Object   response body
    String   response body status       SUCCESS
    Integer  response body calories     305