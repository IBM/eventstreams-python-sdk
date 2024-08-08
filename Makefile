# This makefile is used to make it easier to get the project set up
# to be ready for development work in the local sandbox.
# example: "make setup"

PYTHON=python3
LINT_DIRS=eventstreams_sdk test/unit test/integration examples

setup: deps dev_deps install_project

all: upgrade_pip setup test-unit lint

ci: setup test-unit lint

upgrade_pip:
	${PYTHON} -m pip install --upgrade pip

deps:
	pip install -r requirements.txt

dev_deps:
	pip install -r requirements-dev.txt

install_project:
	pip install -e .

test: test-unit

test-unit:
	pytest --cov=eventstreams_sdk test/unit

test-examples:
	pytest examples

lint:
	${PYTHON} -m pylint ${LINT_DIRS} --exit-zero
	black --check ${LINT_DIRS}

lint-fix:
	black ${LINT_DIRS}

example:
	${PYTHON} example.py
