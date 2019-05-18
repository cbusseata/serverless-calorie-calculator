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
# Install a python module and save it to requirements.txt.  We do this through the virtual environment because otherwise
#  we get every single global module.  We also install it globally so that we don't need to restart the dev environment
#  to use it.
pip-install:
ifndef MODULE
	$(error You must pass a MODULE parameter or we won't know what to install. Example: make pip-install MODULE=<module>)
endif
	@docker exec -i -t calorie-calculator_app bash -c \
		"pip install ${MODULE} && source /app/venv/bin/activate && pip install --ignore-installed --user ${MODULE} && pip freeze --user > requirements.txt && deactivate"
# Uninstall a python module and save it to requirements.txt.  We do this through the virtual environment because otherwise
#  we get every single global module.  We also uninstall it globally so that we don't need to restart the dev environment
#  to pick up the change.
pip-uninstall:
ifndef MODULE
	$(error You must pass a MODULE parameter or we won't know what to uninstall. Example: make pip-uninstall MODULE=<module>)
endif
	@docker exec -i -t calorie-calculator_app bash -c \
		"source /app/venv/bin/activate && pip uninstall -y ${MODULE} && pip freeze --user > requirements.txt && deactivate && pip uninstall -y ${MODULE}"

-include Makefile.d/*.mk
