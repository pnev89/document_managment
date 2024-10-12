
#export PYTHONPATH := .:$(PYTHONPATH)
#export PYTHONPATH := "api"

PACKAGE=src
UNIT_TESTS=tests


# DEV environment
all: style typecheck doccheck unit-tests coverage


style:
		###### Running style analysis ######
		poetry run flake8 $(PACKAGE)

typecheck:
		###### Running static type analysis ######
		poetry run mypy $(PACKAGE)

doccheck:
		###### Running documentation analysis ######
		poetry run pydocstyle -v $(MODULES)

static-tests: style typecheck doccheck

unit-tests:
		###### Running unit tests ######
		poetry run pytest -v $(UNIT_TESTS)/unit_tests

coverage:
		###### Running coverage analysis with JUnit xml export ######
		poetry run pytest --cov-report term-missing --cov-report xml --cov $(PACKAGE)

coverage-html:
		###### Running coverage analysis with html export ######
		poetry run pytest -v --cov-report html --cov $(PACKAGE)
		open htmlcov/index.html

create_docs:
		###### Make Sphinx documentation ######
		sphinx-apidoc -f -o ./docs/source .
		make -C docs clean
		make -C docs html

install_external_dependencies:
		###### Install Poetry's external dependencies
		poetry install --extras recsys

start_elasticsearch:
	docker-compose -f infrastructure/elasticSearch/docker-compose.yml up -d

start_tikaserver:
	docker-compose -f infrastructure/tika/docker-compose.yml up -d




	