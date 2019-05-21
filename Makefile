DOCKER_COMPOSE_PATH := 'ops/docker/docker-compose.yml'

all: down build up
no-cache: down build-no-cache up
up:
	docker-compose -f $(DOCKER_COMPOSE_PATH) up -d
stop:
	docker-compose -f $(DOCKER_COMPOSE_PATH) stop
down:
	docker-compose -f $(DOCKER_COMPOSE_PATH) down -v
build:
	docker-compose -f $(DOCKER_COMPOSE_PATH) build
build-no-cache:
	docker-compose -f $(DOCKER_COMPOSE_PATH) build --no-cache
enter:
	@./ops/docker/scripts/enter.sh ${COMPONENT}
logs:
	docker logs calorie-calculator_app -f

-include Makefile.d/*.mk
