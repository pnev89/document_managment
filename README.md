# Testing projec

This is just a simple example

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

### Setup environment

#### Poetry virtual env

In order to setup the environment you need to
[download poetry](https://python-poetry.org/docs/) and install it using

```zsh
poetry install
```

After that you need to start the environment. For that you should use:

```zsh
poetry shell
```

## How to setup the Mysql server

- Install docker on your computer

- Build docker image:

    ```bash
    docker build -t mysql_db -f database/Dockerfile .
    ```

- Run mysql docker image

    ```bash
    docker run mysql_db
    ```

- Connect the mySql server from within the container
(enter password provided with the command above)

    ```bash
    bash-3.2$ docker exec -it [CONTAINER_ID] /bin/bash
    ```
- To setup mysql do:

    ```bash
    cd docker-entrypoint-initdb.d/
    ```

    ```bash
    mysql -proot
    ```

- The database [classicmodels](database/mysqlsampledatabase.sql) is already created



## How to run API
- Install docker on your computer

- Build docker image:

    ```bash
    docker build -f api/Dockerfile .
    ```

- Run docker container:

    ```bash
    docker run -p 3306:3306 IMAGE_ID
    ```

- Run docker container:

    ```bash
    docker run --env-file .env -p 8000:8000 IMAGE_ID
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

### Setup environment

#### Poetry virtual env

In order to setup the environment you need to
[download poetry](https://python-poetry.org/docs/) and install it using

```zsh
poetry install
```

After that you need to start the environment. For that you should use:

```zsh
poetry shell
```

To install an optional dependencies you can run:

```zsh
poetry install --extras <package>
```

To install all the optional dependencies run:

```zsh
poetry install --extras all
```
