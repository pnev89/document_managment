
#export PYTHONPATH := .:$(PYTHONPATH)
#export PYTHONPATH := "api"

PACKAGE=src
UNIT_TESTS=tests


# DEV environment
all: style typecheck doccheck
start-infrastructure: start_elasticsearch start_tikaserver

style:
		###### Running style analysis ######
		poetry run flake8 $(PACKAGE)

typecheck:
		###### Running static type analysis ######
		poetry run mypy $(PACKAGE)

doccheck:
		###### Running documentation analysis ######
		poetry run pydocstyle -v $(MODULES)

start_elasticsearch:
	docker-compose -f infrastructure/elasticSearch/docker-compose.yml up -d

start_tikaserver:
	docker-compose -f infrastructure/tika/docker-compose.yml up -d


