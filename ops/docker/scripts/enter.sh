#!/bin/bash

COMPONENT=calorie-calculator
CONTAINERS=$(docker ps --no-trunc -f "name=${COMPONENT}" --format "{{.Names}}"| \
    sed "s/^${COMPONENT}_//" | sed "s/_1$//" | tr '\n' ' ')

printf "
  Enter the name of the service that you want to access, choices are:
  ${CONTAINERS}
  Service name: " && read -r SERVICE

docker exec -ti ${COMPONENT}_${SERVICE} /bin/bash; history -c; history -r;

