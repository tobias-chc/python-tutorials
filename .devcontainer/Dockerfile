ARG VARIANT="3.11-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Optional] Section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends git

# Install Poetry
ARG POETRY_VERSION="2.1.0"
ENV POETRY_NO_INTERACTION=1

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && \
    su vscode -c "curl -sSL https://install.python-poetry.org | POETRY_VERSION=${POETRY_VERSION} python3 -"
