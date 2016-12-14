# get the project name from setup.py
PROJECT := $(shell grep 'name=' setup.py | head -n1 | cut -d '=' -f 2 | sed "s/['\", ]//g")
VENV_BIN := $(PWD)/bin
PYTHON := $(VENV_BIN)/python
CC := /usr/bin/gcc

all:
	echo "$(PROJECT)"

build:
	virtualenv .
	$(VENV_BIN)/pip install -U pip
	$(VENV_BIN)/pip install -r requirements.txt
	$(VENV_BIN)/django-admin.py startproject planner_project || echo "planner_project already created"
	$(PYTHON) setup.py build install
	$(PYTHON) setup.py develop
	$(PYTHON) planner_project/manage.py migrate --noinput

shell:
	$(PYTHON) planner_project/manage.py shell_plus

server:
	$(PYTHON) planner_project/manage.py runserver 0:8000

.PHONY: all build shell server
