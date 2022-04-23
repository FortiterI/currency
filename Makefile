SHELL := /bin/bash

manage_py = python app/mange.py

migrate:
	$(manage_py) migrate

shell:
	$(manage_py) shell_plus --print-sql

run:
	$(manage_py) runserver
