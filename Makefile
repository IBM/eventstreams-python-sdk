# This makefile is used to make it easier to get the project set up
# to be ready for development work in the local sandbox.
# example: "make setup"

LINT_DIRS=eventstreams_sdk test/unit examples

setup: deps dev_deps install_project

all: upgrade_pip setup test-unit lint

ci: all

upgrade_pip:
	python -m pip install --upgrade pip

deps:
	pip install -r requirements.txt

dev_deps:
	pip install -r requirements-dev.txt

install_project:
	pip install -e .

test: test-unit

test-unit:
	python -m pytest test/unit

test-examples:
	pytest examples

lint: lint-fix
	pylint ${LINT_DIRS} --exit-zero
	black --check ${LINT_DIRS}

lint-fix:
	black ${LINT_DIRS}

example:
	python example.py
