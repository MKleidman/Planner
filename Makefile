# get the project name from setup.py
PROJECT := $(shell grep 'name=' setup.py | head -n1 | cut -d '=' -f 2 | sed "s/['\", ]//g")
VENV_BIN := $(PWD)/bin
PYTHON := $(VENV_BIN)/python
PROJECT_DIR := $(PWD)/planner_project
CC := /usr/bin/gcc
PROJECT_EXISTS := $(shell ls $(PROJECT_DIR) &>/dev/null; echo $$?)

all:
	@echo "$(PROJECT_EXISTS)"
	@echo "$(PROJECT)"

build:
ifeq ($(PROJECT_EXISTS),1)
	virtualenv .
	$(VENV_BIN)/pip install -U pip
	$(VENV_BIN)/pip install -r requirements.txt
	$(VENV_BIN)/django-admin.py startproject planner_project || echo "planner_project already created"
	$(PYTHON) setup.py build install
	$(PYTHON) setup.py develop
	$(PYTHON) planner_project/manage.py migrate --noinput
	@echo "from planner.settings import *" >> planner_project/planner_project/settings.py
	@echo "" >> planner_project/planner_project/settings.py
else
	@echo '$(PROJECT) exists. Nothing to do for build'
endif

sync:
	$(VENV_BIN)/pip install -U pip
	$(VENV_BIN)/pip install -r requirements.txt
	$(PYTHON) setup.py develop
	$(PYTHON) planner_project/manage.py migrate --noinput


shell:
	$(PYTHON) planner_project/manage.py shell_plus

server:
	$(PYTHON) planner_project/manage.py runserver 0:8000

.PHONY: all build shell server sync
