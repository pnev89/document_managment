# Document management project

This is some simple example of using haystack for document management. Note that this uses OpenAI so you will have to have your own key and use an Env variable to setup (OPEN_API_KEY)

## Setup Running environment
In order to setup the running environment you need to start Apache Tiko and Elastic search containers. For that, please use:

```zsh
make start-infrastructure
```
# Using the project

### Documents
Documents to be ingested into ElasticSearch are within resources/input_docs


# DEVELOPMENT

## Setup dev environment

### Poetry virtual env

In order to setup the environment you need to
[download poetry](https://python-poetry.org/docs/) and install it using

```zsh
poetry install
```

After that you need to start the environment. For that you should use:

```zsh
poetry shell
```

## Precommit Hooks

We use [pre-commit](https://pre-commit.com/) to enforce e.g. code formatting,
linting and type checking prior to committing to the repository.
The `.pre-commit-config.yaml` in the repository includes all of the requirements.
The required packages must be declared on `pyproject.toml`.

Prior to your first commit you need to run

```zsh
pre-commit install
```

If you want to manually run it on all files without a commit

```zsh
pre-commit run --all-files
```