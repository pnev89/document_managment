
export PYTHONPATH := .:$(PYTHONPATH)


PACKAGE=src
UNIT_TESTS=tests


# DEV environment
start-infrastructure: start_elasticsearch start_tikaserver
dev: style typecheck doccheck coverage

.PHONY: all

style:
		###### Running style analysis ######
		poetry run flake8 $(PACKAGE)

typecheck:
		###### Running static type analysis ######
		poetry run mypy $(PACKAGE)

doccheck:
		###### Running documentation analysis ######
		poetry run pydocstyle -v $(MODULES)

unit-tests:
	###### Running unit tests ######
	poetry run pytest -v $(UNIT_TESTS)

coverage:
	###### Running coverage analysis with JUnit xml export ######
	poetry run pytest --cov-report term-missing --cov-report xml --cov $(PACKAGE)

start_elasticsearch:
	docker-compose -f infrastructure/elasticSearch/docker-compose.yml up -d

start_tikaserver:
	docker-compose -f infrastructure/tika/docker-compose.yml up -d




