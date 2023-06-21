
#export PYTHONPATH := .:$(PYTHONPATH)
export PYTHONPATH := "api"

PACKAGE=src
UNIT_TESTS=tests


# DEV environment
all: style typecheck doccheck unit-tests coverage

.PHONY: all

style:
		###### Running style analysis ######
		poetry run flake8 $(RECSYS_API)

typecheck:
		###### Running static type analysis ######
		poetry run mypy $(RECSYS_API)

doccheck:
		###### Running documentation analysis ######
		poetry run pydocstyle -v $(MODULES)

static-tests: style typecheck doccheck

unit-tests:
		###### Running unit tests ######
		poetry run pytest -v $(UNIT_TESTS)/api_testing/unit_tests

coverage:
		###### Running coverage analysis with JUnit xml export ######
		poetry run pytest --cov-report term-missing --cov-report xml --cov $(RECSYS_API)/api

coverage-html:
		###### Running coverage analysis with html export ######
		poetry run pytest -v --cov-report html --cov $(RECSYS_API)
		open htmlcov/index.html

create_docs:
		###### Make Sphinx documentation ######
		sphinx-apidoc -f -o ./docs/source .
		make -C docs clean
		make -C docs html

install_external_dependencies:
		###### Install Poetry's external dependencies
		poetry install --extras recsys

build_airflow:
	docker build -t infrastructure/airflow/airflow-container .

build_sql:
	docker build -t infrastructure/sql_database/mysql-container .

build_spark:
	docker build -t spark-container .

build_https_server_
	docker build -t https-server .

start_infrastructure:
	docker run -d -p 8080:8080 -p 5555:5555 -p 8793:8793 airflow-container
	docker run -d -p 3306:3306 mysql-container
	docker run -it --rm -p 4040:4040 -p 8081:8081 -p 7077:7077 spark-container
