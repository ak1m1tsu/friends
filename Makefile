include .env
export

## help: print this help message
.PHONY: help
help:
	@echo 'Usage:'
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' | sed -e 's/^//'

## env: create venv and install requirements
.PHONY: env
env:
	@python3 -m venv venv

## run: start the application.
.PHONY: run
run:
	./manage.py runserver

## docker/up: up the docker compose stack.
.PHONY: docker/up
docker/up:
	@docker compose up -d --build

## docker/down: down the docker compose stack.
.PHONY: docker/down
docker/down:
	@docker compose down --remove-orphans
